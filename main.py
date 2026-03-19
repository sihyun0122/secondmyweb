import streamlit as st
import random

st.set_page_config(
    page_title="PT 헬스 루틴 생성기",
    page_icon="💪"
)

st.title("💪 디테일 헬스 루틴 생성기")
st.subheader("🔥 진짜 PT처럼 부위별 제대로 조지기")

st.markdown("---")

level = st.selectbox("📊 운동 수준 선택", ["초급 🐣", "중급 🐥", "고급 🦅"])
part = st.selectbox("🏋️ 운동 부위 선택", ["가슴 🟥", "등 🟦", "하체 🟩", "어깨 🟨", "팔 💪", "복근 🟧"])

arm_part = None
if part == "팔 💪":
    arm_part = st.radio("💪 팔 부위 선택", ["이두 💪", "삼두 🔥"])

st.markdown("---")

# 🔥 세트 설정
if "초급" in level:
    reps = "10회 × 3세트"
    lv = "초급"
elif "중급" in level:
    reps = "12회 × 4세트"
    lv = "중급"
else:
    reps = "15회 × 5세트"
    lv = "고급"

# 🔥 가슴 (윗/중앙/아랫)
chest = {
"윗가슴":{
"초급":["인클라인 머신 프레스"],
"중급":["인클라인 덤벨 프레스"],
"고급":["인클라인 바벨 프레스"]
},
"중앙":{
"초급":["머신 체스트 프레스"],
"중급":["벤치프레스"],
"고급":["덤벨 벤치프레스"]
},
"아랫가슴":{
"초급":["디클라인 푸쉬업"],
"중급":["딥스"],
"고급":["디클라인 벤치프레스"]
}
}

# 🔥 어깨 (전/측/후)
shoulder = {
"전면":{
"초급":["프론트 레이즈"],
"중급":["덤벨 숄더 프레스"],
"고급":["아놀드 프레스"]
},
"측면":{
"초급":["사이드 레터럴 레이즈"],
"중급":["덤벨 레터럴 레이즈"],
"고급":["케이블 레터럴 레이즈"]
},
"후면":{
"초급":["리어 델트 머신"],
"중급":["리어 델트 플라이"],
"고급":["벤트오버 레터럴 레이즈"]
}
}

# 🔥 등 (광배 / 중앙)
back = {
"광배":{
"초급":["랫풀다운"],
"중급":["풀업"],
"고급":["와이드 풀업"]
},
"중앙":{
"초급":["시티드 로우"],
"중급":["바벨 로우"],
"고급":["티바 로우"]
}
}

# 🔥 팔
arm = {
"이두 💪":{
"초급":["덤벨 컬"],
"중급":["바벨 컬"],
"고급":["프리처 컬"]
},
"삼두 🔥":{
"초급":["벤치 딥스"],
"중급":["트라이셉스 푸쉬다운"],
"고급":["스컬 크러셔"]
}
}

# 🔥 하체 / 복근
lower = {
"하체 🟩":["스쿼트","런지","레그 프레스","레그 컬"],
"복근 🟧":["크런치","플랭크","레그 레이즈","러시안 트위스트"]
}

# 🚀 실행
if st.button("🚀 루틴 생성"):

    st.balloons()

    st.markdown("## 💪 오늘의 운동 루틴")

    # 가슴
    if part == "가슴 🟥":
        st.markdown("### 🟥 가슴 (상/중/하 균형)")

        for k in chest:
            ex = random.choice(chest[k][lv])
            st.write(f"🏋️ {k} : {ex} - {reps}")

    # 어깨
    elif part == "어깨 🟨":
        st.markdown("### 🟨 어깨 (전/측/후 균형)")

        for k in shoulder:
            ex = random.choice(shoulder[k][lv])
            st.write(f"🏋️ {k} : {ex} - {reps}")

    # 등
    elif part == "등 🟦":
        st.markdown("### 🟦 등 (광배 + 중앙)")

        for k in back:
            ex = random.choice(back[k][lv])
            st.write(f"🏋️ {k} : {ex} - {reps}")

        # 하나 더 추가
        extra = random.choice(back["중앙"][lv])
        st.write(f"🔥 추가 : {extra} - {reps}")

    # 팔
    elif part == "팔 💪":
        st.markdown(f"### 💪 {arm_part}")

        for ex in arm[arm_part][lv]:
            st.write(f"🏋️ {ex} - {reps}")

    # 하체 / 복근
    else:
        st.markdown(f"### {part}")

        for ex in random.sample(lower[part], 3):
            st.write(f"🏋️ {ex} - {reps}")

    st.markdown("---")

    st.info("⚠️ 부위 자극 느끼는 게 가장 중요합니다!")

    st.success("🔥 오늘 운동 완료! 근성장 +1")

st.markdown("---")
st.caption("💪 PT 디테일 루틴 생성기")
