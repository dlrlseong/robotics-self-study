# 맥 환경 설정 (Apple Silicon)

MuJoCo, roboticstoolbox-python, Drake 모두 Apple Silicon(arm64)용 설치 파일이 있습니다. Intel 맥에서는 Drake가 공식 지원 대상이 아니므로 MuJoCo 위주로 진행하세요.

## 설치

Drake는 애플 기본 파이썬이 아니라 Homebrew 파이썬이 필요합니다(Drake 공식 문서). 처음부터 Homebrew 파이썬으로 가상환경을 만드는 편이 편합니다.

```bash
# Homebrew가 없으면 https://brew.sh 안내대로 먼저 설치
brew install python
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 심화 (8주차 이후, Tedrake 강의용)
pip install -r requirements-extra.txt
```

가상환경 폴더 `.venv/`는 `.gitignore`에 들어 있어 커밋되지 않습니다.

## 확인

```bash
python scripts/check_env.py
```

## MuJoCo 뷰어를 맥에서 띄울 때

`mujoco.viewer.launch_passive`를 쓰는 스크립트는 맥에서 `python` 대신 `mjpython`으로 실행해야 합니다(MuJoCo 파이썬 문서). `mjpython`은 `mujoco` 패키지와 함께 설치됩니다.

```bash
mjpython my_script.py
```

## 로봇 모델

[MuJoCo Menagerie](https://github.com/google-deepmind/mujoco_menagerie)를 `third_party/` 아래에 내려받아 쓰세요. 이 폴더는 `.gitignore`로 제외되어 있어 제3자 저장소가 이 레포에 섞이지 않습니다.

```bash
mkdir -p third_party
git clone https://github.com/google-deepmind/mujoco_menagerie third_party/mujoco_menagerie
```

`franka_emika_panda`와 `universal_robots_ur5e` 폴더를 쓰면 됩니다.

## 팁

- 노트북이 팬이 없는 기종이면 오래 도는 시뮬레이션에서 느려질 수 있습니다. 반복 실험은 데스크톱 쪽에 맡기고 코드는 GitHub로 동기화하세요.
- ROS 2는 이 커리큘럼에 필요하지 않습니다.
