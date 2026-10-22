# 로보틱스 8주 독학

*Modern Robotics* (Lynch & Park)를 주 교재로, 로봇 팔의 기구학·동역학·제어·계획을 6주에 끝내고 7~8주차에 이동로봇의 상태추정과 SLAM으로 넓히는 독학 커리큘럼입니다. 컴퓨터공학 전공자가 맥(Apple Silicon)에서 파이썬과 MuJoCo로 실습하는 것을 가정했습니다.

## 이 레포의 쓰는 법

1. 이 레포를 **Fork하거나 Template으로 복제**합니다.
2. [`docs/mac-setup.md`](docs/mac-setup.md)대로 환경을 만들고 `python scripts/check_env.py`로 확인합니다.
3. 주차별 폴더(`weeks/week-NN-*`)의 `README.md`를 순서대로 따라갑니다.
4. 공부하면서 같은 폴더의 `notes/`(공부 노트), `proof/`(공부 인증), `practice/`(실습 코드)를 채웁니다.
5. 끝나면 [`blog/`](blog/)에 후기 초안을 정리합니다.

## 진도표

| 주차 | 주제 | 교재 읽기 | 완료일 |
| --- | --- | --- | --- |
| 1 | [배위공간과 회전](weeks/week-01-configuration-space-rotation/README.md) | 67쪽 |  |
| 2 | [강체 운동과 순기구학](weeks/week-02-rigid-body-forward-kinematics/README.md) | 49쪽 |  |
| 3 | [속도 기구학과 역기구학](weeks/week-03-velocity-inverse-kinematics/README.md) | 47쪽 |  |
| 4 | [동역학과 궤적 생성](weeks/week-04-dynamics-trajectory/README.md) | 50쪽 |  |
| 5 | [로봇 제어와 중간 프로젝트](weeks/week-05-robot-control/README.md) | 49쪽 |  |
| 6 | [모션 플래닝](weeks/week-06-motion-planning/README.md) | 44쪽 |  |
| 7 | [이동로봇 모델과 상태추정](weeks/week-07-mobile-robots-state-estimation/README.md) | 16쪽 |  |
| 8 | [SLAM과 캡스톤](weeks/week-08-slam-capstone/README.md) | — |  |

## 폴더 구조

```text
.
├── README.md
├── LICENSE
├── requirements.txt          # 필수 패키지
├── requirements-extra.txt    # 심화(Drake)
├── docs/
│   ├── curriculum.md         # 전체 일정표
│   ├── resources.md          # 강의·교재·도구 링크
│   ├── mac-setup.md          # 맥 환경 설정
│   └── public-checklist.md   # 공개 전 점검표
├── materials/                # 교재 PDF를 본인이 따로 두는 곳 (git 제외)
├── weeks/
│   └── week-NN-*/
│       ├── README.md         # 그 주의 강의·쪽수·실습·체크포인트
│       ├── notes/            # 공부 노트
│       ├── proof/            # 공부 인증
│       └── practice/         # 실습 코드
├── templates/                # 노트·인증 템플릿
├── blog/                     # 블로그 후기 초안
└── scripts/
    ├── check_env.py          # 환경 점검
    └── public_check.py       # push 전 공개 안전성 점검
```

## 교재와 저작권

교재 PDF, 강의 슬라이드, *Probabilistic Robotics* 본문은 이 레포에 **포함하지 않습니다**. 저자 사이트의 무료 PDF는 개인 사용만 허용되고 재배포가 금지되어 있습니다. 링크만 [`docs/resources.md`](docs/resources.md)에 두었으니 각자 내려받아 `materials/`에 넣으세요(`.gitignore`가 막아 줍니다). 쪽수 범위는 2017년 5월 사전판 기준입니다.

## 라이선스

직접 작성한 문서와 코드는 [MIT](LICENSE)입니다. 링크된 교재·강의·소프트웨어의 권리는 각 저작권자에게 있습니다.
