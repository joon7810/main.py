import streamlit as st

st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# MBTI별 단짝 포켓몬 데이터
# 이미지 주소는 PokeAPI sprites 저장소의 공식 아트워크 파일을 사용합니다.
# 앱 자체는 외부 API를 호출하지 않으며, 이미지 표시 때만 인터넷이 필요합니다.
# ------------------------------------------------------------
POKEMON = {
    "ENFP": {
        "name": "피카츄", "english": "Pikachu", "id": 25,
        "type": "전기", "type_emoji": "⚡",
        "feature": "호기심이 많고 에너지가 넘치는 분위기 메이커",
        "why": "새로운 일을 보면 함께 뛰어들어 줄 든든한 모험 친구예요.\\n밝은 에너지로 아이디어를 더 신나게 펼쳐 줘요.",
        "color": "#F6C94D",
    },
    "ENFJ": {
        "name": "푸린", "english": "Jigglypuff", "id": 39,
        "type": "노말 · 페어리", "type_emoji": "🎤",
        "feature": "다정하고 표현력이 풍부한 작은 가수",
        "why": "친구들의 기분을 살피고 따뜻하게 응원해 줘요.\\n함께 노래하고 이야기하다 보면 모두가 편안해져요.",
        "color": "#F3A8C8",
    },
    "ENTP": {
        "name": "파오리", "english": "Farfetch'd", "id": 83,
        "type": "노말 · 비행", "type_emoji": "🦆",
        "feature": "자기만의 도구를 활용하는 재치 있는 전략가",
        "why": "엉뚱한 아이디어도 재미있는 도전으로 바꿔 줘요.\\n서로 생각을 주고받으며 새로운 방법을 찾아낼 수 있어요.",
        "color": "#B6D5A8",
    },
    "ENTJ": {
        "name": "갸라도스", "english": "Gyarados", "id": 130,
        "type": "물 · 비행", "type_emoji": "🌊",
        "feature": "강한 추진력과 압도적인 존재감을 가진 포켓몬",
        "why": "목표를 정하면 힘차게 나아가는 모습을 닮았어요.\\n큰 계획도 용기 있게 시작하도록 서로 북돋아 줘요.",
        "color": "#8CC8E8",
    },
    "ESFP": {
        "name": "이상해꽃", "english": "Venusaur", "id": 3,
        "type": "풀 · 독", "type_emoji": "🌻",
        "feature": "햇살과 자연의 기운을 품은 든든한 친구",
        "why": "함께하는 시간을 풍성하고 즐겁게 만들어 줘요.\\n활동적인 하루에도 편안히 쉴 수 있는 안정감을 더해요.",
        "color": "#A8D5A0",
    },
    "ESFJ": {
        "name": "럭키", "english": "Chansey", "id": 113,
        "type": "노말", "type_emoji": "💗",
        "feature": "다른 이를 돌보는 것을 좋아하는 상냥한 포켓몬",
        "why": "작은 변화도 알아차리고 먼저 챙겨 주는 모습이 잘 어울려요.\\n서로를 응원하며 따뜻한 팀워크를 만들 수 있어요.",
        "color": "#F6B7C9",
    },
    "ESTP": {
        "name": "리자몽", "english": "Charizard", "id": 6,
        "type": "불꽃 · 비행", "type_emoji": "🔥",
        "feature": "모험을 좋아하고 행동력이 뛰어난 포켓몬",
        "why": "망설이기보다 직접 경험하며 배우는 성향과 잘 맞아요.\\n새로운 장소와 도전을 함께 누비는 콤비가 될 수 있어요.",
        "color": "#F3A36D",
    },
    "ESTJ": {
        "name": "코뿌리", "english": "Rhydon", "id": 112,
        "type": "땅 · 바위", "type_emoji": "🪨",
        "feature": "튼튼한 몸과 힘으로 앞장서는 믿음직한 포켓몬",
        "why": "맡은 일을 책임감 있게 해내는 점이 서로 닮았어요.\\n계획을 세우고 차근차근 목표를 이루는 팀이 되어 줘요.",
        "color": "#C5B8A5",
    },
    "INFP": {
        "name": "이브이", "english": "Eevee", "id": 133,
        "type": "노말", "type_emoji": "🌸",
        "feature": "가능성이 많고 마음이 따뜻한 포켓몬",
        "why": "자신만의 속도와 개성을 소중히 여기는 모습이 닮았어요.\\n편안한 곁에서 상상력과 가능성을 마음껏 키울 수 있어요.",
        "color": "#D9B28C",
    },
    "INFJ": {
        "name": "가디안", "english": "Gardevoir", "id": 282,
        "type": "에스퍼 · 페어리", "type_emoji": "🌙",
        "feature": "소중한 이를 지키려는 마음이 깊은 포켓몬",
        "why": "말하지 않은 마음까지 헤아리려는 다정함이 잘 어울려요.\\n복잡한 생각을 차분히 나누고 서로에게 힘이 되어 줘요.",
        "color": "#B9C6E8",
    },
    "INTP": {
        "name": "폴리곤", "english": "Porygon", "id": 137,
        "type": "노말", "type_emoji": "🧩",
        "feature": "디지털 공간에서 활동하는 독특하고 논리적인 포켓몬",
        "why": "궁금한 것을 깊이 파고들며 원리를 찾는 성향과 잘 맞아요.\\n함께 관찰하고 가설을 세우며 재미있는 답을 찾아봐요.",
        "color": "#A9C9E8",
    },
    "INTJ": {
        "name": "뮤츠", "english": "Mewtwo", "id": 150,
        "type": "에스퍼", "type_emoji": "🔮",
        "feature": "뛰어난 지능과 전략적인 사고를 지닌 포켓몬",
        "why": "큰 그림을 생각하고 목표를 향해 계획하는 점이 닮았어요.\\n복잡한 문제도 차분히 분석하며 해결책을 찾는 단짝이에요.",
        "color": "#C6B5E8",
    },
    "ISFP": {
        "name": "치코리타", "english": "Chikorita", "id": 152,
        "type": "풀", "type_emoji": "🌿",
        "feature": "온화하고 주변을 편안하게 해 주는 포켓몬",
        "why": "조용한 순간과 소소한 아름다움을 즐기는 모습이 잘 어울려요.\\n서두르지 않고 함께 산책하며 마음을 나눌 수 있어요.",
        "color": "#B6D9A3",
    },
    "ISFJ": {
        "name": "밀탱크", "english": "Miltank", "id": 241,
        "type": "노말", "type_emoji": "🐄",
        "feature": "주변을 보살피고 안정감을 주는 포켓몬",
        "why": "늘 곁을 지키고 세심하게 챙기는 다정함이 닮았어요.\\n익숙한 일상 속에서 서로에게 든든한 편이 되어 줘요.",
        "color": "#E9B7C4",
    },
    "ISTP": {
        "name": "팬텀", "english": "Gengar", "id": 94,
        "type": "고스트 · 독", "type_emoji": "👻",
        "feature": "장난기 있고 상황 대처가 빠른 포켓몬",
        "why": "필요할 때 직접 손을 움직여 문제를 해결하는 모습과 잘 맞아요.\\n예상 밖의 상황도 유연하고 재치 있게 넘길 수 있어요.",
        "color": "#B8A5D9",
    },
    "ISTJ": {
        "name": "거북왕", "english": "Blastoise", "id": 9,
        "type": "물", "type_emoji": "🐢",
        "feature": "차분하고 믿음직하며 꾸준히 실력을 쌓는 포켓몬",
        "why": "약속과 순서를 지키며 꾸준히 해내는 점이 닮았어요.\\n급하게 서두르지 않고 한 걸음씩 목표에 도달하는 단짝이에요.",
        "color": "#8EC5E8",
    },
}

TYPE_ORDER = [
    ["ISTJ", "ISFJ", "INFJ", "INTJ"],
    ["ISTP", "ISFP", "INFP", "INTP"],
    ["ESTP", "ESFP", "ENFP", "ENTP"],
    ["ESTJ", "ESFJ", "ENFJ", "ENTJ"],
]

st.markdown("""
<style>
:root { --cream:#fffaf0; --butter:#ffe8a3; --gold:#e6a817; --ink:#493a26; }
html, body, [class*="css"] { font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif; }
.stApp { background: linear-gradient(180deg,#fff9e9 0%,#fffdf7 48%,#fff3ce 100%); color:var(--ink); }
.block-container { max-width: 850px; padding-top: 2rem; padding-bottom: 3rem; }
.hero { text-align:center; padding:1.8rem 1rem 1.4rem; border:2px solid #f5d989; border-radius:28px;
        background:rgba(255,255,255,.72); box-shadow:0 10px 28px rgba(151,112,35,.09); }
.hero .eyebrow { font-size:1rem; font-weight:900; color:#a8750a; letter-spacing:.08em; }
.hero h1 { font-family:'Malgun Gothic',sans-serif; font-size:clamp(2.2rem,6vw,3.5rem); line-height:1.2; color:#6b4c13; margin:.5rem 0; }
.hero p { font-size:1.12rem; margin:.3rem 0; }
.section-title { font-size:1.4rem; font-weight:900; color:#6b4c13; margin:1.5rem 0 .7rem; }
div[data-testid="stButton"] button { border-radius:15px; border:2px solid #f0d27c; background:#fffdf6; color:#5d481e;
    font-size:1.05rem; font-weight:900; min-height:3.2rem; transition:all .15s ease; }
div[data-testid="stButton"] button:hover { border-color:#e0a800; background:#fff0b9; color:#4b3610; transform:translateY(-1px); }
.poke-card { border:2px solid #f0d27c; background:rgba(255,255,255,.86); border-radius:28px; overflow:hidden;
    box-shadow:0 14px 32px rgba(141,103,24,.12); margin-top:1rem; }
.poke-top { padding:1.5rem 1.4rem 1rem; text-align:center; background:linear-gradient(135deg,#fff3c7,#fffaf0); }
.poke-top .small-label { color:#967019; font-weight:900; font-size:.95rem; }
.poke-top h2 { font-family:'Malgun Gothic',sans-serif; font-size:clamp(2rem,5vw,2.8rem); margin:.2rem 0; color:#594014; }
.poke-top .eng { font-size:1.05rem; color:#8c7446; font-weight:700; }
.poke-img { display:block; width:min(250px,75%); height:auto; max-height:250px; object-fit:contain; margin:.5rem auto .2rem;
    filter:drop-shadow(0 10px 5px rgba(106,82,33,.12)); animation:popIn .65s cubic-bezier(.2,1.4,.4,1) both; }
.poke-body { padding:1.3rem 1.5rem 1.6rem; }
.chips { display:flex; gap:.55rem; flex-wrap:wrap; justify-content:center; margin:.4rem 0 1.2rem; }
.chip { border-radius:999px; background:#fff0b9; border:1px solid #f0d27c; padding:.45rem .9rem; font-weight:900; font-size:1rem; }
.info-title { color:#93670c; font-weight:900; font-size:1.08rem; margin:1rem 0 .3rem; }
.info-text { font-size:1.08rem; line-height:1.85; color:#51432c; }
.why-box { background:#fff8df; border-left:5px solid #e6b52d; border-radius:12px; padding:1rem 1.1rem; font-size:1.08rem; line-height:1.9; white-space:pre-line; }
.footer-note { text-align:center; color:#987e4b; font-size:.88rem; padding-top:1.5rem; }
div[data-testid="stAlert"] { border-radius:15px; }
@keyframes popIn { 0%{transform:scale(.45) rotate(-8deg);opacity:0} 70%{transform:scale(1.08) rotate(3deg);opacity:1} 100%{transform:scale(1) rotate(0);opacity:1} }
@media (max-width:600px) {
 .block-container { padding-left:1rem; padding-right:1rem; }
 .hero { padding:1.3rem .7rem; border-radius:22px; }
 .poke-body { padding:1rem; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="eyebrow">✨ 나와 꼭 맞는 포켓몬 찾기 ✨</div>
  <h1>MBTI 단짝 포켓몬</h1>
  <p>내 성격과 잘 어울리는 포켓몬은 누구일까요?</p>
  <p>아래에서 MBTI를 고르고 단짝을 만나 보세요!</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">🌼 1. 내 MBTI를 골라 주세요</div>', unsafe_allow_html=True)
st.caption("MBTI는 성격을 가볍게 살펴보는 재미있는 도구예요. 결과는 정답이 아니라 즐거운 놀이랍니다!")

# 선택 상태를 유지하면서 버튼을 누르면 결과가 표시됩니다.
if "selected_mbti" not in st.session_state:
    st.session_state.selected_mbti = None

for row_idx, row in enumerate(TYPE_ORDER):
    cols = st.columns(4)
    for col_idx, mbti in enumerate(row):
        with cols[col_idx]:
            label = ("✓ " if st.session_state.selected_mbti == mbti else "") + mbti
            if st.button(label, key=f"mbti_{mbti}", use_container_width=True):
                st.session_state.selected_mbti = mbti
                st.rerun()

selected = st.session_state.selected_mbti

if selected:
    p = POKEMON[selected]
    st.markdown('<div class="section-title">🎉 2. 두근두근… 당신의 단짝은!</div>', unsafe_allow_html=True)
    st.balloons()

    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{p['id']}.png"
    why = p["why"].replace("\\n", "\n")
    st.markdown(f"""
    <div class="poke-card">
      <div class="poke-top">
        <div class="small-label">💛 {selected}의 단짝 포켓몬 💛</div>
        <h2>{p['name']}</h2>
        <div class="eng">{p['english']}</div>
        <img class="poke-img" src="{image_url}" alt="{p['name']} 공식 아트워크"
             onerror="this.onerror=null;this.style.display='none';document.getElementById('image-fallback').style.display='block';">
        <div id="image-fallback" style="display:none;font-size:5rem;padding:1.5rem;">✨</div>
      </div>
      <div class="poke-body">
        <div class="chips">
          <span class="chip">{p['type_emoji']} 타입: {p['type']}</span>
          <span class="chip">💫 MBTI: {selected}</span>
        </div>
        <div class="info-title">🌟 포켓몬 특징</div>
        <div class="info-text">{p['feature']}</div>
        <div class="info-title">💌 왜 잘 어울릴까요?</div>
        <div class="why-box">{why.replace(chr(10), '<br>')}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    if st.button("🔄 다른 MBTI도 만나 보기", use_container_width=True):
        st.session_state.selected_mbti = None
        st.rerun()

st.markdown("""
<div class="footer-note">
  포켓몬 이미지는 PokeAPI sprites 저장소의 공식 아트워크를 표시합니다.<br>
  MBTI와 포켓몬의 연결은 재미를 위한 창작 설정입니다.
</div>
""", unsafe_allow_html=True)
