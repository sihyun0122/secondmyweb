import streamlit as st
import random

st.set_page_config(
    page_title="헬스 루틴 생성기",
    page_icon="💪"
)

st.title("💪 헬스 루틴 생성기")
st.subheader("🔥 운동 방법까지 배우는 실전 루틴")

st.markdown("---")

level = st.selectbox("📊 운동 수준", ["초급 🐣", "중급 🐥", "고급 🦅"])
part = st.selectbox("🏋️ 운동 부위", ["가슴 🟥", "어깨 🟨", "등 🟦", "팔 💪"])

arm_part = None
if part == "팔 💪":
    arm_part = st.radio("💪 선택", ["이두 💪", "삼두 🔥"])

st.markdown("---")

# 세트 설정
if "초급" in level:
    reps = "10회 × 3세트"
    lv = "초급"
elif "중급" in level:
    reps = "12회 × 4세트"
    lv = "중급"
else:
    reps = "15회 × 5세트"
    lv = "고급"

# 🔥 운동 설명 데이터
exercise = {

"벤치프레스":"가슴 중앙 운동\n👉 바벨을 가슴까지 내린 후 가슴 힘으로 밀어 올리기",
"인클라인 프레스":"윗가슴 운동\n👉 벤치를 기울이고 위쪽 가슴 자극 집중",
"딥스":"아랫가슴 운동\n👉 상체를 앞으로 기울이면 가슴 자극 증가",

"프론트 레이즈":"어깨 전면\n👉 팔을 앞으로 들어 올리기",
"사이드 레터럴 레이즈":"어깨 측면\n👉 옆으로 들어 어깨 넓이 만들기",
"리어 델트 플라이":"어깨 후면\n👉 숙여서 뒤쪽 어깨 자극",

"랫풀다운":"광배근 운동\n👉 가슴 쪽으로 당기며 등 사용",
"바벨 로우":"등 중앙\n👉 허리 숙이고 배쪽으로 당기기",

"덤벨 컬":"이두 운동\n👉 팔꿈치 고정 후 들어올리기",
"바벨 컬":"이두 운동\n👉 반동 없이 천천히 수행",

"푸쉬다운":"삼두 운동\n👉 팔꿈치 고정 후 아래로 밀기",
"스컬 크러셔":"삼두 운동\n👉 팔을 굽혀서 자극 집중"
}

# 루틴 생성
if st.button("🚀 루틴 생성"):

    st.balloons()

    st.markdown("## 💪 오늘의 운동 루틴")

    # 가슴
    if part == "가슴 🟥":
        routine = ["인클라인 프레스","벤치프레스","딥스"]

        st.markdown("### 🟥 가슴 (상/중/하 균형)")

    # 어깨
    elif part == "어깨 🟨":
        routine = ["프론트 레이즈","사이드 레터럴 레이즈","리어 델트 플라이"]

        st.markdown("### 🟨 어깨 (전/측/후 균형)")

    # 등
    elif part == "등 🟦":
        routine = ["랫풀다운","바벨 로우"]

        st.markdown("### 🟦 등 (광배 + 중앙)")

    # 팔
    elif part == "팔 💪":

        st.markdown(f"### 💪 {arm_part}")

        if arm_part == "이두 💪":
            routine = ["덤벨 컬","바벨 컬"]
        else:
            routine = ["푸쉬다운","스컬 크러셔"]

    # 출력
    for ex in routine:

        st.markdown(f"### 🏋️ {ex}")
        st.write(f"👉 {reps}")

        st.info(exercise[ex])

        st.markdown("---")

    st.success("🔥 오늘 운동 완료! 진짜 성장 시작이다.")

st.markdown("---")
st.caption("💪 헬스 루틴 생성기 (이미지 없는 버전)")
