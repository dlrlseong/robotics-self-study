# 2주차 · 강체 운동과 순기구학

**핵심 질문.** 회전과 이동을 4×4 행렬 하나로 묶고, 관절 하나씩의 움직임을 곱해 팔 끝 위치를 어떻게 구하는가.

읽기 분량: **49쪽 (정독 36 + 훑기 13)**

## 1. 강의

- [Coursera Course 1 후반 (Ch.3) + Course 2 앞부분 (Ch.4)](https://www.coursera.org/learn/modernrobotics-course2)
- [저자 영상 Ch.3 재생목록의 7~11번 (약 22분)](https://www.youtube.com/playlist?list=PLggLP4f-rq01NLHOh2vVPPJZ0rxkbVFNc)
- [저자 영상 Ch.4 재생목록 (약 14분)](https://www.youtube.com/playlist?list=PLggLP4f-rq00efLcgMcG1m4k5CKlgRcGh)
- [보조: Stanford CS223A 강의 2–5 (D-H 표기 사용)](https://see.stanford.edu/Course/CS223A)

## 2. 교재 읽기 (Modern Robotics)

쪽수는 2017년 5월 사전판의 교재 인쇄 쪽수입니다. 판이 다르면 쪽수가 어긋날 수 있으니 목차로 대조하세요. 읽는 순서대로 정리했습니다.

| 교재 쪽 | 구분 | 내용 |
| --- | --- | --- |
| pp.89–112 | 정독 | §3.3–3.5 동차변환, 트위스트, 렌치, 요약 |
| pp.113–114 | 훑기 | §3.6 소프트웨어 |
| pp.137–139 | 훑기 | Ch.4 도입 |
| pp.140–151 | 정독 | §4.1 Product of Exponentials 공식 두 가지 형태 |
| pp.152–159 | 훑기 | §4.2 URDF, 요약, 소프트웨어 |

## 3. 연습문제

- Ch.3 pp.116–136 중 3~4문항 (트위스트, 동차변환)
- Ch.4 pp.160–170 중 3문항

## 4. 실습

- [ ] 교재 p.147 UR5 예제의 매개변수로 `FKinSpace`를 직접 구현
- [ ] `roboticstoolbox`의 UR5 모델과 여러 관절각에서 팔 끝 자세 비교 (두 라이브러리의 좌표계 정의가 다를 수 있으니 기준 프레임부터 확인)

코드는 [`practice/`](practice/)에 둡니다.

## 5. 체크포인트

직접 구현한 순기구학이 `modern_robotics`의 `FKinSpace`와 수치 허용 오차 안에서 일치한다.

## 6. 기록

- 공부 노트: [`notes/`](notes/)
- 공부 인증: [`proof/`](proof/)
