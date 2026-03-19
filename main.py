import streamlit as st

st.set_page_config(
    page_title="헬스 루틴 + 운동 설명",
    page_icon="💪"
)

st.title("💪 헬스 루틴 생성기")
st.subheader("🔥 운동 방법까지 완벽하게 배우기")

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
elif "중급" in level:
    reps = "12회 × 4세트"
else:
    reps = "15회 × 5세트"

# 🔥 운동 설명 + 이미지 경로
exercise_data = {

"벤치프레스":{
"img":"images/bench.png",
"desc":"""
1. 벤치에 누워 발을 바닥에 고정합니다  
2. 어깨보다 약간 넓게 바벨을 잡습니다  
3. 가슴 중앙까지 천천히 내립니다  
4. 가슴의 힘으로 밀어 올립니다  
👉 팔이 아니라 가슴으로 밀어내는 느낌!
"""
},

"인클라인 덤벨 프레스":{
"img":"images/incline.png",
"desc":"""
1. 벤치를 30~45도로 설정합니다  
2. 덤벨을 들고 가슴 위에서 시작  
3. 천천히 내려서 가슴을 늘려줍니다  
4. 윗가슴으로 밀어 올립니다  
👉 윗가슴 자극 집중!
"""
},

"딥스":{
"img":"images/dips.png",
"desc":"""
1. 평행봉을 잡고 몸을 띄웁니다  
2. 상체를 약간 앞으로 기울입니다  
3. 팔을 굽혀 몸을 내립니다  
4. 가슴과 삼두로 밀어 올립니다  
👉 상체 기울이면 가슴 자극 ↑
"""
},

"사이드 레터럴 레이즈":{
"img":"images/lateral.png",
"desc":"""
1. 덤벨을 들고 양옆에 둡니다  
2. 팔을 옆으로 들어 올립니다  
3. 어깨 높이까지만 올립니다  
👉 반동 없이 천천히!
"""
},

"프론트 레이즈":{
"img":"images/front.png",
"desc":"""
1. 덤벨을 허벅지 앞에 둡니다  
2. 팔을 앞으로 들어 올립니다  
3. 어깨 높이까지 올립니다  
👉 전면 어깨 집중
"""
},

"리어 델트 플라이":{
"img":"images/rear.png",
"desc":"""
1. 허리를 숙이고 덤벨을 듭니다  
2. 팔을 양옆으로 벌립니다  
3. 후면 어깨에 집중  
👉 등 말고 어깨 뒤쪽!
"""
},

"랫풀다운":{
"img":"images/latpulldown.png",
"desc":"""
1. 바를 넓게 잡습니다  
2. 가슴 쪽으로 당깁니다  
3. 천천히 올립니다  
👉 팔이 아니라 등으로 당기기!
"""
},

"바벨 로우":{
"img":"images/row.png",
"desc":"""
1. 허리를 숙이고 바벨을 잡습니다  
2. 배 쪽으로 당깁니다  
3. 등을 수축합니다  
👉 등 중앙 자극!
"""
},

"덤벨 컬":{
"img":"images/curl.png",
"desc":"""
1. 덤벨을 양손에 듭니다  
2. 팔꿈치를 고정하고 올립니다  
3. 천천히 내립니다  
👉 반동 금지!
"""
},

"트라이셉스 푸쉬다운":{
"img":"images/triceps.png",
"desc":"""
1. 케이블을 잡습니다  
2. 팔꿈치를 고정  
3. 아래로 밀어냅니다  
👉 삼두 수축 집중!
"""
}

}

# 루틴 생성
if st.button("🚀 루틴 생성"):

    st.balloons()

    st.markdown("## 💪 오늘의 운동")

    if part == "가슴 🟥":
        routine = ["인클라인 덤벨 프레스","벤치프레스","딥스"]

    elif part == "어깨 🟨":
        routine = ["프론트 레이즈","사이드 레터럴 레이즈","리어 델트 플라이"]

    elif part == "등 🟦":
        routine = ["랫풀다운","바벨 로우"]

    elif part == "팔 💪":
        if arm_part == "이두 💪":
            routine = ["덤벨 컬"]
        else:
            routine = ["트라이셉스 푸쉬다운"]

    # 출력
    for ex in routine:

        st.markdown(f"### 🏋️ {ex}")
        st.write(f"👉 {reps}")

        # 이미지 자리
        st.image(exercise_data[ex]["img"], width=300)

        # 설명
        st.info(exercise_data[ex]["desc"])

        st.markdown("---")

    st.success("🔥 자세까지 완벽하면 진짜 성장 시작!")

st.markdown("---")
st.caption("💪 헬스 루틴 + 운동 설명 앱")
