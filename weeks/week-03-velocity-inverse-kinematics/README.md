# 3주차 · 속도 기구학과 역기구학

**핵심 질문.** 관절 속도와 팔 끝 속도의 관계(야코비안)는 무엇인가. 특이점에서 무슨 일이 생기는가. 목표 자세에서 관절각을 어떻게 거꾸로 구하는가.

읽기 분량: **47쪽 (정독 30 + 훑기 17)**

## 1. 강의

- [Coursera Course 2 (Ch.4–7)의 Ch.5–6 부분](https://www.coursera.org/learn/modernrobotics-course2)
- [저자 영상 Ch.5 재생목록 (약 35분)](https://www.youtube.com/playlist?list=PLggLP4f-rq00oA7lrv6dS5C15RYjqj4Zi)
- [저자 영상 Ch.6 재생목록 (약 14분)](https://www.youtube.com/playlist?list=PLggLP4f-rq01fi62ek1BoV1yiPHLL3Vt-)
- [보조: Stanford CS223A 강의 6–8 (야코비안)](https://see.stanford.edu/Course/CS223A)

## 2. 교재 읽기 (Modern Robotics)

쪽수는 교재 인쇄 쪽수이고, PDF 쪽수는 2017년 5월 사전판 기준으로 인쇄 쪽수에 18을 더한 값입니다. 판이 다르면 쪽수가 어긋날 수 있으니 목차로 대조하세요.

| 구분 | 교재 쪽 | PDF 쪽 | 내용 |
| --- | --- | --- | --- |
| 정독 | pp.178–199 | 196–217 | §5.1–5.4 공간·몸체 야코비안, 정력학, 특이점, 조작성 |
| 정독 | pp.226–233 | 244–251 | §6.2–6.3 수치 역기구학, 역속도 기구학 |
| 훑기 | pp.171–177 | 189–195 | Ch.5 도입 |
| 훑기 | p.200 | 218 | §5.5 요약 |
| 훑기 | pp.219–225 | 237–243 | §6.1 해석적 역기구학 |
| 훑기 | pp.234–235 | 252–253 | §6.4–6.6 |

## 3. 연습문제

- Ch.5 pp.202–218 중 3~4문항
- Ch.6 pp.236–244 중 2~3문항

## 4. 실습

- [ ] `JacobianSpace` 직접 구현
- [ ] 2R 평면 팔의 조작성 타원을 matplotlib으로 그리기 (특이점에 가까울수록 타원이 찌그러짐)
- [ ] pp.227–231의 뉴턴-랩슨 알고리즘을 그대로 따라 `IKinSpace` 구현
- [ ] MuJoCo 설치 후 MuJoCo Menagerie의 Franka Panda 또는 UR5e 불러오기 (docs/mac-setup.md)

코드는 [`practice/`](practice/)에 둡니다.

## 5. 체크포인트

목표 자세를 주면 역기구학으로 관절각을 구하고, MuJoCo 팔이 그 자세를 취하는지 오차까지 확인한다.

## 6. 기록

- 공부 노트: [`notes/`](notes/)
- 공부 인증: [`proof/`](proof/)
