# 공개(push) 전 점검표

`python scripts/public_check.py`를 실행하면 아래 항목을 자동으로 확인합니다. 결과가 `OK`일 때만 push하세요.

- [ ] 교재 PDF, 강의 슬라이드, 유료 책 본문이 추적 파일에 없다 (`git ls-files | grep -i pdf`)
- [ ] 비밀키·토큰·`.env`가 없다
- [ ] 개인 이메일, 집 주소, 전화번호가 없다 (`git log --format='%ae' | sort -u`로 커밋 이메일도 확인)
- [ ] 절대 경로(`/Users/이름/`)가 코드와 노트북 출력에 없다
- [ ] 5MB를 넘는 파일이 없다
- [ ] 노트북의 출력 셀을 지웠다
- [ ] 증거 이미지에 교재 본문 페이지 전체가 찍혀 있지 않다
- [ ] 라이선스의 저작권자 이름을 본인으로 바꿨다

## 커밋 이메일

공개 레포의 커밋에는 이메일이 그대로 남습니다. GitHub의 `Settings → Emails`에서 "Keep my email addresses private"를 켜고, 표시되는 `ID+이름@users.noreply.github.com` 주소를 쓰세요.

```bash
git config user.name  "본인 GitHub ID"
git config user.email "ID+이름@users.noreply.github.com"
```
