import streamlit as st
import random

st.set_page_config(page_title="PT 루틴 생성기", page_icon="💪")

st.title("💪 진짜 PT 헬스 루틴 생성기")
st.subheader("🔥 난이도 + 부위별 맞춤 루틴")

st.markdown("---")

level = st.selectbox("📊 운동 수준", ["초급 🐣", "중급 🐥", "고급 🦅"])
part = st.selectbox("🏋️ 운동 부위", ["가슴 🟥", "어깨 🟨", "등 🟦", "팔 💪"])

arm_part = None
if part == "팔 💪":
    arm_part = st.radio("💪 팔 선택", ["이두 💪", "삼두 🔥"])

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

# 🔥 운동 DB (난이도별 완전 다르게 구성)
db = {

"가슴 🟥":{
"윗가슴":{
"초급":["인클라인 머신 프레스","인클라인 푸쉬업"],
"중급":["인클라인 덤벨 프레스","인클라인 벤치프레스"],
"고급":["인클라인 바벨 프레스","스미스 인클라인 프레스"]
},
"중앙":{
"초급":["머신 체스트 프레스","푸쉬업"],
"중급":["벤치프레스","덤벨 프레스"],
"고급":["파워 벤치프레스","덤벨 벤치프레스"]
},
"아랫가슴":{
"초급":["디클라인 푸쉬업"],
"중급":["딥스","디클라인 덤벨 프레스"],
"고급":["디클라인 벤치프레스","웨이트 딥스"]
}
},

"어깨 🟨":{
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
},

"등 🟦":{
"광배":{
"초급":["랫풀다운","어시스트 풀업"],
"중급":["풀업","와이드 랫풀다운"],
"고급":["와이드 풀업","중량 풀업"]
},
"중앙":{
"초급":["시티드 로우"],
"중급":["바벨 로우","원암 덤벨 로우"],
"고급":["티바 로우","펜들레이 로우"]
}
}

}

# 팔 DB
arm_db = {

"이두 💪":{
"초급":["덤벨 컬","밴드 컬"],
"중급":["바벨 컬","해머 컬","케이블 컬"],
"고급":["프리처 컬","컨센트레이션 컬","EZ바 컬"]
},

"삼두 🔥":{
"초급":["벤치 딥스","밴드 푸쉬다운"],
"중급":["트라이셉스 푸쉬다운","오버헤드 익스텐션"],
"고급":["스컬 크러셔","클로즈그립 벤치프레스","케이블 익스텐션"]
}

}

# 🚀 실행
if st.button("🚀 루틴 생성"):

    st.balloons()
    st.markdown("## 💪 오늘의 루틴")

    # 가슴
    if part == "가슴 🟥":
        st.markdown("### 🟥 가슴 (상/중/하 분할)")
        for k in db[part]:
            ex = random.choice(db[part][k][lv])
            st.write(f"🏋️ {k} → {ex} ({reps})")

    # 어깨
    elif part == "어깨 🟨":
        st.markdown("### 🟨 어깨 (전/측/후 분할)")
        for k in db[part]:
            ex = random.choice(db[part][k][lv])
            st.write(f"🏋️ {k} → {ex} ({reps})")

    # 등
    elif part == "등 🟦":
        st.markdown("### 🟦 등 (광배 + 중앙)")
        for k in db[part]:
            ex = random.choice(db[part][k][lv])
            st.write(f"🏋️ {k} → {ex} ({reps})")

        # 추가 한 개 더 (강도 증가)
        extra = random.choice(db[part]["중앙"][lv])
        st.write(f"🔥 추가 → {extra} ({reps})")

    # 팔
    elif part == "팔 💪":
        st.markdown(f"### 💪 {arm_part}")

        exercises = arm_db[arm_part][lv]

        selected = random.sample(exercises, min(3, len(exercises)))

        for ex in selected:
            st.write(f"🏋️ {ex} ({reps})")

    st.markdown("---")

    st.info("⚠️ 난이도에 맞는 무게 선택이 핵심입니다!")

    st.success("🔥 이 루틴이면 진짜 성장한다.")

st.markdown("---")
st.caption("💪 PT 루틴 생성기 (완성판)")
