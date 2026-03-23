import streamlit as st
import random

st.set_page_config(page_title="Training", page_icon="⚫", layout="centered")

# 🎨 드라마틱 스타일
st.markdown("""
<style>
body {
    background-color: #0b0c10;
}
.block-container {
    padding-top: 2rem;
}
.title {
    font-size: 42px;
    font-weight: 700;
    letter-spacing: 2px;
    text-align: center;
    color: #ffffff;
}
.subtitle {
    text-align: center;
    color: #8a8f98;
    margin-bottom: 30px;
}
.section {
    margin-top: 30px;
    margin-bottom: 10px;
    font-size: 18px;
    color: #c5c6c7;
}
.card {
    background: #111217;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 14px;
    border-left: 3px solid #66fcf1;
}
.exercise {
    font-size: 20px;
    font-weight: 600;
    color: #ffffff;
}
.meta {
    font-size: 13px;
    color: #66fcf1;
    margin-top: 6px;
}
.desc {
    margin-top: 10px;
    font-size: 14px;
    color: #c5c6c7;
    line-height: 1.6;
}
button[kind="primary"] {
    background-color: #66fcf1 !important;
    color: black !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# 🎯 타이틀
st.markdown('<div class="title">TRAINING SESSION</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">오늘의 루틴을 선택하세요</div>', unsafe_allow_html=True)

# 선택
level = st.selectbox("LEVEL", ["초급", "중급", "고급"])
part = st.selectbox("FOCUS", ["가슴", "어깨", "등", "팔"])

arm_part = None
if part == "팔":
    arm_part = st.radio("DETAIL", ["이두", "삼두"])

# 세트
if level == "초급":
    reps = "10 × 3"
elif level == "중급":
    reps = "12 × 4"
else:
    reps = "15 × 5"

# 튜토리얼
tutorial = {
"벤치프레스":"가슴으로 밀어낸다. 어깨 개입 최소화.",
"인클라인 프레스":"윗가슴을 수축한다.",
"딥스":"상체를 기울이면 가슴 자극이 깊어진다.",
"프론트 레이즈":"전면 삼각근 집중.",
"사이드 레터럴":"반동 없이 측면 자극.",
"리어 델트":"후면을 의식한다.",
"랫풀다운":"광배로 당긴다.",
"풀업":"몸을 끌어올린다.",
"바벨 로우":"등 중앙을 수축한다.",
"덤벨 컬":"이두 수축 유지.",
"바벨 컬":"반동 없이 천천히.",
"푸쉬다운":"삼두를 끝까지 밀어낸다.",
"스컬 크러셔":"팔을 접었다 펴며 집중."
}

# DB
db = {
"가슴":["인클라인 프레스","벤치프레스","딥스"],
"어깨":["프론트 레이즈","사이드 레터럴","리어 델트"],
"등":["랫풀다운","풀업","바벨 로우"]
}

arm_db = {
"이두":["덤벨 컬","바벨 컬"],
"삼두":["푸쉬다운","스컬 크러셔"]
}

# 실행
if st.button("START"):

    st.markdown('<div class="section">TODAY</div>', unsafe_allow_html=True)

    if part != "팔":
        exercises = db[part]
    else:
        exercises = arm_db[arm_part]

    for ex in exercises:
        st.markdown(f"""
        <div class="card">
            <div class="exercise">{ex}</div>
            <div class="meta">{reps}</div>
            <div class="desc">{tutorial[ex]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section">END</div>', unsafe_allow_html=True)
