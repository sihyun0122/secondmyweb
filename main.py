import streamlit as st
import random

st.set_page_config(page_title="PT 루틴", page_icon="💪", layout="centered")

# 🎨 커스텀 CSS
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-title {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    color: #00ffcc;
}
.sub {
    text-align: center;
    color: #aaa;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    border: 1px solid #2c2f36;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}
.exercise {
    font-size: 20px;
    font-weight: bold;
    color: #00ffcc;
}
.desc {
    color: #ddd;
    margin-top: 8px;
}
.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 10px;
    background: #00ffcc;
    color: black;
    font-size: 12px;
    margin-bottom: 10px;
}
button[kind="primary"] {
    background-color: #00ffcc !important;
    color: black !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 🎯 타이틀
st.markdown('<div class="main-title">💪 PT 루틴 생성기</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">🔥 간지나게 운동하자</div>', unsafe_allow_html=True)

st.markdown("---")

# 🎛 선택 UI
level = st.selectbox("📊 운동 수준", ["초급 🐣", "중급 🐥", "고급 🦅"])
part = st.selectbox("🏋️ 운동 부위", ["가슴 🟥", "어깨 🟨", "등 🟦", "팔 💪"])

arm_part = None
if part == "팔 💪":
    arm_part = st.radio("💪 팔 선택", ["이두 💪", "삼두 🔥"])

st.markdown("---")

# 🎯 세트 설정
if "초급" in level:
    reps = "10회 × 3세트"
    lv = "초급"
elif "중급" in level:
    reps = "12회 × 4세트"
    lv = "중급"
else:
    reps = "15회 × 5세트"
    lv = "고급"

# 📘 튜토리얼
tutorial = {
"벤치프레스":"가슴으로 밀어내기. 어깨 힘 쓰지 말기.",
"인클라인 덤벨 프레스":"윗가슴 집중.",
"딥스":"상체 기울이면 가슴 자극.",
"프론트 레이즈":"전면 어깨 자극.",
"사이드 레터럴 레이즈":"반동 없이.",
"리어 델트 플라이":"후면 어깨 집중.",
"랫풀다운":"등으로 당기기.",
"풀업":"광배 자극.",
"바벨 로우":"등 중앙 수축.",
"덤벨 컬":"팔꿈치 고정.",
"바벨 컬":"반동 금지.",
"트라이셉스 푸쉬다운":"삼두 수축.",
"스컬 크러셔":"삼두 집중."
}

# 📊 운동 DB
db = {
"가슴 🟥":["인클라인 덤벨 프레스","벤치프레스","딥스"],
"어깨 🟨":["프론트 레이즈","사이드 레터럴 레이즈","리어 델트 플라이"],
"등 🟦":["랫풀다운","풀업","바벨 로우"]
}

arm_db = {
"이두 💪":["덤벨 컬","바벨 컬"],
"삼두 🔥":["트라이셉스 푸쉬다운","스컬 크러셔"]
}

# 🚀 실행
if st.button("🚀 루틴 생성"):

    st.balloons()

    st.markdown("## 🔥 오늘의 루틴")

    # 일반 부위
    if part != "팔 💪":
        for ex in db[part]:
            st.markdown(f"""
            <div class="card">
                <div class="badge">{lv}</div>
                <div class="exercise">🏋️ {ex}</div>
                <div class="desc">👉 {reps}<br>{tutorial[ex]}</div>
            </div>
            """, unsafe_allow_html=True)

    # 팔
    else:
        for ex in arm_db[arm_part]:
            st.markdown(f"""
            <div class="card">
                <div class="badge">{lv}</div>
                <div class="exercise">💪 {ex}</div>
                <div class="desc">👉 {reps}<br>{tutorial[ex]}</div>
            </div>
            """, unsafe_allow_html=True)

    st.success("🔥 이 루틴이면 진짜 몸 바뀐다.")

st.markdown("---")
st.caption("💪 PT 루틴 앱 (간지 UI 버전)")
