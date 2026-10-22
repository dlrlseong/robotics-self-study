# 1주차 · 배위공간과 회전

**핵심 질문.** 로봇의 상태를 숫자 몇 개로 쓸 수 있는가. 회전행렬은 숫자가 9개인데 왜 자유도는 3인가.

읽기 분량: **67쪽 (정독 38 + 훑기 29)**

## 1. 강의

- [Coursera Course 1 앞부분 (Ch.2–3)](https://www.coursera.org/learn/modernrobotics-course1)
- [저자 영상 Ch.2 재생목록 (약 28분)](https://www.youtube.com/playlist?list=PLggLP4f-rq01z8VLqhDC94W2nWpWpZoMj)
- [저자 영상 Ch.3 재생목록의 앞 6개 (약 19분)](https://www.youtube.com/playlist?list=PLggLP4f-rq01NLHOh2vVPPJZ0rxkbVFNc)

## 2. 교재 읽기 (Modern Robotics)

쪽수는 2017년 5월 사전판의 교재 인쇄 쪽수입니다. 판이 다르면 쪽수가 어긋날 수 있으니 목차로 대조하세요. 읽는 순서대로 정리했고, pp.38–58은 Ch.2 연습문제 구간이라 건너뜁니다.

| 교재 쪽 | 구분 | 내용 |
| --- | --- | --- |
| pp.1–11 | 훑기 | Ch.1 전체, Ch.2 도입 |
| pp.12–22 | 정독 | §2.1–2.2 강체·로봇의 자유도, Grübler 공식 |
| pp.23–31 | 훑기 | §2.3–2.4 위상, 제약 |
| pp.32–37 | 정독 | §2.5–2.6 작업공간, 요약 |
| pp.59–67 | 훑기 | Ch.3 도입, §3.1 평면 운동 |
| pp.68–88 | 정독 | §3.2 회전행렬, 각속도, 회전의 지수좌표 |

## 3. 연습문제

- Ch.2 pp.38–58 중 3~4문항 (자유도 계산, Grübler)
- Ch.3 pp.116–136 중 회전 관련 2문항

## 4. 실습

- [ ] numpy로 회전행렬 생성, 직교성·행렬식 검사 함수 구현
- [ ] 축-각도에서 회전행렬로 가는 지수 맵(로드리게스 공식)과 그 역(로그) 구현
- [ ] `modern_robotics`의 `MatrixExp3`, `MatrixLog3`와 결과 비교

코드는 [`practice/`](practice/)에 둡니다.

## 5. 체크포인트

무작위 회전행렬 100개에 대해 `exp(log(R))`이 원래 R과 수치 허용 오차 안에서 같다.

## 6. 기록

- 공부 노트: [`notes/`](notes/)
- 공부 인증: [`proof/`](proof/)
