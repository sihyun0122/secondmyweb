import streamlit as st
import random

st.set_page_config(
    page_title="헬스 루틴 + 운동 설명",
    page_icon="💪"
)

st.title("💪 헬스 루틴 + 운동 설명")
st.subheader("🔥 운동 방법까지 완벽하게!")

st.markdown("---")

level = st.selectbox("📊 운동 수준", ["초급 🐣", "중급 🐥", "고급 🦅"])
part = st.selectbox("🏋️ 운동 부위", ["가슴 🟥", "어깨 🟨", "등 🟦", "팔 💪"])

arm_part = None
if part == "팔 💪":
    arm_part = st.radio("💪 선택", ["이두 💪", "삼두 🔥"])

st.markdown("---")

# 세트
if "초급" in level:
    reps = "10회 × 3세트"
    lv = "초급"
elif "중급" in level:
    reps = "12회 × 4세트"
    lv = "중급"
else:
    reps = "15회 × 5세트"
    lv = "고급"

# 🔥 운동 데이터 (설명 + 이미지 포함)
exercise_info = {

"벤치프레스":{
"desc":"가슴 중앙을 자극하는 대표 운동. 가슴으로 밀어내는 느낌 중요!",
"img":"https://images.unsplash.com/photo-1599058917212-d750089bc07e"
},

"인클라인 덤벨 프레스":{
"desc":"윗가슴을 집중적으로 자극하는 운동",
"img":"https://images.unsplash.com/photo-1583454110551-21f2fa2afe61"
},

"딥스":{
"desc":"아랫가슴과 삼두를 동시에 자극",
"img":"https://images.unsplash.com/photo-1594737625785-cb0bbd6c7c63"
},

"사이드 레터럴 레이즈":{
"desc":"어깨 측면을 넓게 만들어주는 핵심 운동",
"img":"https://images.unsplash.com/photo-1605296867304-46d5465a13f1"
},

"프론트 레이즈":{
"desc":"어깨 전면 발달",
"img":"https://images.unsplash.com/photo-1581009137042-c552e485697a"
},

"리어 델트 플라이":{
"desc":"어깨 후면 자극 (자세 중요!)",
"img":"https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b"
},

"랫풀다운":{
"desc":"광배근을 넓게 만드는 기본 운동",
"img":"https://images.unsplash.com/photo-1598970434795-0c54fe7c0642"
},

"바벨 로우":{
"desc":"등 두께를 키워주는 운동",
"img":"https://images.unsplash.com/photo-1605296867724-fa87a8ef7d12"
},

"덤벨 컬":{
"desc":"이두근 기본 운동",
"img":"https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e"
},

"트라이셉스 푸쉬다운":{
"desc":"삼두를 키우는 대표 운동",
"img":"https://images.unsplash.com/photo-1605296867424-35fc25c9212a"
}

}

# 루틴
if st.button("🚀 루틴 생성"):

    st.balloons()

    st.markdown("## 💪 오늘의 운동")

    routine = []

    # 가슴
    if part == "가슴 🟥":
        routine = ["인클라인 덤벨 프레스", "벤치프레스", "딥스"]

    # 어깨
    elif part == "어깨 🟨":
        routine = ["프론트 레이즈", "사이드 레터럴 레이즈", "리어 델트 플라이"]

    # 등
    elif part == "등 🟦":
        routine = ["랫풀다운", "바벨 로우"]

    # 팔
    elif part == "팔 💪":
        if arm_part == "이두 💪":
            routine = ["덤벨 컬"]
        else:
            routine = ["트라이셉스 푸쉬다운"]

    # 출력
    for ex in routine:

        st.markdown(f"### 🏋️ {ex}")
        st.write(f"👉 {reps}")

        st.image(exercise_info[ex]["img"], width=300)

        st.info(exercise_info[ex]["desc"])

        st.markdown("---")

    st.success("🔥 자세까지 완벽하면 진짜 성장 시작이다!")

st.markdown("---")
st.caption("💪 운동 설명 포함 헬스 앱")
