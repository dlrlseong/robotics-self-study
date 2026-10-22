# 7주차 · 이동로봇 모델과 상태추정

**핵심 질문.** 센서에 노이즈가 있을 때 로봇이 '내가 어디 있는가'를 확률분포로 어떻게 갱신하는가.

읽기 분량: **16쪽 (정독 12 + 훑기 4)**

## 1. 강의

- [Stachniss, Online Training – Mobile Robotics (Probability Primer → Bayes Filter → Kalman Filter & EKF → Particle Filter & MCL 순서. 개별 영상은 페이지에서 제목으로 찾기)](https://www.ipb.uni-bonn.de/online-training-robotics/)
- [저자 영상 Ch.13 재생목록의 4번(모델링), 11번(오도메트리)](https://www.youtube.com/playlist?list=PLggLP4f-rq00uzTEwsywVcTF2fJ2YqAXX)
- [Stachniss EKF 강의 슬라이드](https://www.ipb.uni-bonn.de/html/teaching/photo12-2021/2021-pho2-14-ekf.pptx.pdf)

## 2. 교재 읽기 (Modern Robotics)

쪽수는 2017년 5월 사전판의 교재 인쇄 쪽수입니다. 판이 다르면 쪽수가 어긋날 수 있으니 목차로 대조하세요. 읽는 순서대로 정리했습니다.

| 교재 쪽 | 구분 | 내용 |
| --- | --- | --- |
| pp.513–514 | 정독 | §13.1 바퀴형 이동로봇의 종류 |
| pp.520–527 | 정독 | §13.3.1 유니사이클·차동 구동 모델 |
| pp.542–545 | 훑기 | §13.3.4 비홀로노믹 피드백 제어 |
| pp.546–547 | 정독 | §13.4 오도메트리 |

**별도 교재 Probabilistic Robotics (Thrun, Burgard, Fox).** 베이즈 필터, 가우시안 필터(칼만·EKF), 비모수 필터(파티클), 로봇 운동 모델 장을 읽습니다. 책은 무료 공개가 아니므로 이 레포에 포함하지 않았고 쪽수도 적지 않았습니다. 본인이 가진 판의 목차에 맞춰 직접 채워 넣으세요.

## 3. 연습문제

- Ch.13 pp.555–564 중 1~2문항 (차동 구동 운동학)

## 4. 실습

- [ ] 차동 구동 로봇의 운동 모델로 궤적 시뮬레이션
- [ ] 노이즈 섞인 랜드마크 거리·방위각 측정을 생성
- [ ] EKF 위치추정과 파티클 필터(MCL) 위치추정 구현

코드는 [`practice/`](practice/)에 둡니다.

## 5. 체크포인트

추정 궤적과 참값의 오차를 그래프로 그리고, EKF 공분산 타원(3σ)이 실제 오차를 대부분 포함하는지 확인한다.

## 6. 기록

- 공부 노트: [`notes/`](notes/)
- 공부 인증: [`proof/`](proof/)
