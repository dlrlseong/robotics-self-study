#!/usr/bin/env python3
"""실습 환경 점검: 필수 패키지를 불러와 버전을 출력한다."""
import importlib
import sys

REQUIRED = ["numpy", "scipy", "matplotlib", "modern_robotics", "mujoco", "roboticstoolbox"]
OPTIONAL = ["pydrake"]


def check(name):
    try:
        mod = importlib.import_module(name)
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}: {exc}"
    return True, getattr(mod, "__version__", "version unknown")


def main():
    print(f"Python {sys.version.split()[0]}")
    failed = 0
    for name in REQUIRED:
        ok, info = check(name)
        failed += not ok
        print(f"[{'OK' if ok else 'FAIL'}] {name}: {info}")
    for name in OPTIONAL:
        ok, info = check(name)
        print(f"[{'OK' if ok else 'skip'}] {name} (선택): {info}")
    if failed:
        print(f"\n필수 패키지 {failed}개가 실패했습니다. docs/mac-setup.md를 확인하세요.")
        return 1
    print("\n환경 점검 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
