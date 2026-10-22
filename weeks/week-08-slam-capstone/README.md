# 8주차 · SLAM과 캡스톤

**핵심 질문.** 지도도 모르고 내 위치도 모를 때 둘을 동시에 어떻게 추정하는가.

읽기 분량: **교재 읽기 없음**

## 1. 강의

- [Stachniss, Robot Mapping 2013/14 재생목록 (EKF-SLAM, 최소제곱, 그래프 기반 SLAM)](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN_)
- [Robot Mapping 강좌 홈 (슬라이드는 이메일 요청)](https://www.ipb.uni-bonn.de/robot-mapping/)
- [선택: 교재 저자의 캡스톤 안내 영상](https://youtu.be/Q1CekpBW6Js)

## 2. 교재 읽기 (Modern Robotics)

쪽수는 교재 인쇄 쪽수이고, PDF 쪽수는 2017년 5월 사전판 기준으로 인쇄 쪽수에 18을 더한 값입니다. 판이 다르면 쪽수가 어긋날 수 있으니 목차로 대조하세요.

| 구분 | 교재 쪽 | PDF 쪽 | 내용 |
| --- | --- | --- | --- |
| 선택 | pp.548–552 | 566–570 | §13.5 이동 조작 (교재 쪽수 읽기는 이 주에 필수가 아님) |

**별도 교재 Probabilistic Robotics.** 점유격자 지도와 SLAM 장을 읽습니다(쪽수 미기재, 본인 판의 목차 참조).

## 3. 연습문제

- 없음

## 4. 실습

- [ ] 2D 포즈그래프를 최소제곱(가우스-뉴턴)으로 최적화
- [ ] 캡스톤 택 1. (A) 조작: MuJoCo Panda에서 RRT와 계산토크로 장애물을 피하는 집어 옮기기. (B) 이동: EKF-SLAM 또는 포즈그래프 최적화. (C) 교재 저자의 캡스톤 개념(이동 조작) 따라 해 보기

코드는 [`practice/`](practice/)에 둡니다.

## 5. 체크포인트

처음 보는 사람이 README만 보고 캡스톤 데모를 재현할 수 있다.

## 6. 기록

- 공부 노트: [`notes/`](notes/)
- 공부 인증: [`proof/`](proof/)
