#!/usr/bin/env python3
"""공개(push) 전 안전성 점검. git이 추적하는 파일만 검사한다.

사용: python scripts/public_check.py
"""
import os
import re
import subprocess
import sys
from pathlib import Path

MAX_BYTES = 5 * 1024 * 1024
SECRET_PATTERNS = {
    "GitHub 토큰": r"gh[pousr]_[A-Za-z0-9]{30,}",
    "AWS 키": r"AKIA[0-9A-Z]{16}",
    "개인키": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    "Slack 토큰": r"xox[baprs]-[A-Za-z0-9-]{10,}",
    "API 키 할당": r"(?i)(api[_-]?key|secret|passwd|password|token)\s*[=:]\s*[\"'][^\"'\s]{8,}[\"']",
}
ABS_PATH = re.compile(r"(?:/Users/[A-Za-z0-9._-]+|/home/[A-Za-z0-9._-]+|C:\\Users\\[A-Za-z0-9._-]+)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ALLOWED_EMAIL_SUFFIX = ("users.noreply.github.com", "example.com")
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".zip", ".gz"}
SELF = "scripts/public_check.py"


def tracked():
    out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout
    return [p for p in out.decode().split("\0") if p]


def goto_repo_root():
    here = Path(__file__).resolve().parent
    res = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=here
    )
    if res.returncode != 0:
        print("git 저장소가 아닙니다. 먼저 git init 으로 저장소를 만드세요.")
        sys.exit(2)
    os.chdir(res.stdout.strip())


def main():
    goto_repo_root()
    problems = []
    for rel in tracked():
        path = Path(rel)
        if not path.exists():
            continue
        low = rel.lower()
        if low.endswith(".pdf"):
            problems.append(f"PDF가 추적 중 (교재·슬라이드 재배포 금지 가능): {rel}")
        if low.endswith((".mp4", ".mov", ".avi", ".mkv")):
            problems.append(f"동영상이 추적 중: {rel}")
        if path.name.startswith(".env") or low.endswith((".pem", ".key", ".p12")):
            problems.append(f"비밀 파일로 의심: {rel}")
        if path.stat().st_size > MAX_BYTES:
            problems.append(f"5MB 초과: {rel} ({path.stat().st_size // 1024} KB)")
        if rel == SELF or path.suffix.lower() in BINARY_EXT:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pat in SECRET_PATTERNS.items():
            if re.search(pat, text):
                problems.append(f"{label} 패턴 발견: {rel}")
        for m in ABS_PATH.finditer(text):
            problems.append(f"개인 절대경로 발견: {rel}: {m.group(0)}")
        for m in EMAIL.finditer(text):
            if not m.group(0).lower().endswith(ALLOWED_EMAIL_SUFFIX):
                problems.append(f"이메일 발견: {rel}: {m.group(0)}")

    emails = subprocess.run(
        ["git", "log", "--format=%ae%n%ce"], capture_output=True, text=True
    ).stdout.split()
    for e in sorted(set(emails)):
        if not e.lower().endswith(ALLOWED_EMAIL_SUFFIX):
            problems.append(f"커밋 이메일이 공개됩니다: {e} (noreply 주소로 바꾸세요)")

    if problems:
        print("공개 전에 확인할 항목:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("OK: 점검 항목에서 문제를 찾지 못했습니다. (자동 점검은 완전하지 않으니 docs/public-checklist.md도 확인하세요)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
