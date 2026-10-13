import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI x 포켓몬 단짝 찾기",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. 커스텀 CSS (따뜻한 크림/노란색 톤, 큰 글씨, 초보자용 가독성 디자인)
st.markdown(
    """
    <style>
    /* 전체 배경 및 기본 폰트 설정 */
    .stApp {
        background-color: #FFFDF0;
        font-family: 'Pretendard', 'Apple SD Gothic Neo', sans-serif;
        color: #333333;
    }
    
    /* 상단 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        color: #D97706;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    .sub-title {
        text-align: center;
        font-size: 1.15rem;
        color: #B45309;
        margin-bottom: 25px;
    }

    /* 포켓몬 결과 카드 스타일 */
    .pokemon-card {
        background-color: #FFFFFF;
        border: 3px solid #FCD34D;
        border-radius: 24px;
        padding: 28px 24px;
        box-shadow: 0 10px 25px rgba(217, 119, 6, 0.12);
        margin-top: 15px;
        margin-bottom: 25px;
    }

    .pokemon-name-kr {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1F2937;
        margin-bottom: 4px;
        display: inline-block;
    }

    .pokemon-name-en {
        font-size: 1.2rem;
        color: #6B7280;
        font-weight: 600;
        margin-left: 8px;
    }

    /* 타입 태그 바 */
    .type-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        color: white;
        font-weight: bold;
        font-size: 1rem;
        margin-right: 6px;
        margin-bottom: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    /* 상세 설명 박스 */
    .section-box {
        background-color: #FEF3C7;
        border-radius: 16px;
        padding: 16px 20px;
        margin-top: 15px;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #B45309;
        margin-bottom: 8px;
    }

    .reason-list {
        font-size: 1.1rem;
        line-height: 1.75;
        color: #374151;
        margin: 0;
        padding-left: 20px;
    }

    /* 궁합 박스 */
    .chemistry-box {
        background-color: #ECFDF5;
        border: 2px dashed #34D399;
        border-radius: 16px;
        padding: 14px 18px;
        margin-top: 15px;
        text-align: center;
        font-size: 1.15rem;
        font-weight: 700;
        color: #065F46;
    }

    /* 스트림릿 기본 컴포넌트 폰트 키우기 */
    div[data-baseweb="select"] {
        font-size: 1.2rem !important;
    }
    
    label {
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        color: #92400E !important;
    }
    </style>
    """,
    unsafe_unsafe_html=True if hasattr(st, 'unsafe_html') else True,
    unsafe_allow_html=True
)

# 3. 16가지 MBTI별 포켓몬 데이터베이스 (공식 포켓몬 아트워크 고화질 URL 적용)
POKEMON_DATA = {
    "ENFP": {
        "mbti_title": "재기발랄한 활동가 (ENFP)",
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "types": [("전기", "#F7D02C")],
        "features": "통통 튀는 무한한 에너지를 뿜어내며, 언제나 주변 사람들에게 긍정적이고 밝은 활력을 전파합니다.",
        "reason": [
            "풍부한 호기심과 친화력으로 누구와도 금방 절친이 됩니다.",
            "톡톡 튀는 아이디어와 열정으로 주변 분위기를 환하게 밝힙니다.",
            "지루한 일상에서 벗어나 새로운 모험을 함께 떠나기 최고의 단짝입니다!"
        ],
        "match": "INTJ (루카리오)"
    },
    "INFP": {
        "mbti_title": "열정적인 중재자 (INFP)",
        "ko_name": "이브이",
        "en_name": "Eevee",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "types": [("노말", "#A8A878")],
        "features": "무한한 가능성과 따뜻한 감수성을 품고 있으며, 무언가에 한번 몰입하면 놀라운 집중력을 보여줍니다.",
        "reason": [
            "자신의 가치관과 이상을 중요하게 여기는 낭만주의자입니다.",
            "어떤 환경에서든 자신만의 다채로운 포텐셜을 발휘할 수 있습니다.",
            "마음 속 깊은 진심을 알아봐 주는 조용하고 든든한 영혼의 단짝입니다."
        ],
        "match": "ENFJ (토게키스)"
    },
    "ENTP": {
        "mbti_title": "뜨거운 논쟁을 즐기는 변론가 (ENTP)",
        "ko_name": "로토무",
        "en_name": "Rotom",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/479.png",
        "types": [("전기", "#F7D02C"), ("유령", "#70559B")],
        "features": "창의적이고 기발하며, 어디로 튈지 모르는 엉뚱함과 장난기 넘치는 영리함을 가지고 있습니다.",
        "reason": [
            "고정관념을 깨부수고 언제나 신선하고 새로운 시각을 제안합니다.",
            "다양한 형태로 변신하듯 호기심 많은 지적 호기심 왕입니다.",
            "당신의 기발한 상상력을 이해하고 함께 재미난 일을 만들어낼 완벽한 파트너입니다."
        ],
        "match": "INFJ (뮤)"
    },
    "INTJ": {
        "mbti_title": "용의주도한 전략가 (INTJ)",
        "ko_name": "루카리오",
        "en_name": "Lucario",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "types": [("격투", "#C22E28"), ("강철", "#B7B7CE")],
        "features": "냉철한 통찰력과 강한 신념을 가졌으며, 목표를 정하면 치밀하게 계획하여 완벽하게 완수합니다.",
        "reason": [
            "상대방의 파동(마음)을 정확히 읽어내는 깊은 직관력을 가졌습니다.",
            "감정에 휘둘리지 않고 항상 합리적이고 신뢰할 수 있는 방향을 제시합니다.",
            "서로의 영역을 존중하며 함께 성장할 수 있는 든든한 조력자입니다."
        ],
        "match": "ENFP (피카츄)"
    },
    "INFJ": {
        "mbti_title": "선을 행하는 통찰가 (INFJ)",
        "ko_name": "뮤",
        "en_name": "Mew",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "types": [("에스퍼", "#F95587")],
        "features": "신비롭고 온화하며, 타인의 마음을 누구보다 깊게 이해하는 깊은 배려심을 지니고 있습니다.",
        "reason": [
            "말하지 않아도 마음을 느끼는 뛰어난 공감 능력과 통찰력을 지녔습니다.",
            "평화와 완벽한 조화를 추구하며 진정성 있는 관계를 중요하게 여깁니다.",
            "당신의 고민과 꿈을 진심으로 응원해 주는 따뜻한 수호천사 같은 존재입니다."
        ],
        "match": "ENTP (로토무)"
    },
    "ENFJ": {
        "mbti_title": "정의로운 사회운동가 (ENFJ)",
        "ko_name": "토게키스",
        "en_name": "Togekiss",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "types": [("페어리", "#D685AD"), ("비행", "#A98FF3")],
        "features": "따뜻한 보듬음과 리더십으로 사람들에게 희망과 다정한 행복을 전파합니다.",
        "reason": [
            "주변 사람들의 행복을 자신의 행복처럼 기뻐하는 베풀기 대장입니다.",
            "갈등이 생기면 서로 원만하게 조율하여 분위기를 훈훈하게 만듭니다.",
            "언제나 당신의 편이 되어 긍정적인 에너지를 한가득 선물해 줍니다."
        ],
        "match": "INFP (이브이)"
    },
    "INTP": {
        "mbti_title": "아이디어가 넘치는 아이디어상가 (INTP)",
        "ko_name": "후딘",
        "en_name": "Alakazam",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "types": [("에스퍼", "#F95587")],
        "features": "비상한 두뇌와 압도적인 분석력으로 복잡한 문제를 명쾌하게 풀어냅니다.",
        "reason": [
            "호기심이 생기면 깊이 탐구하는 지적 탐구심의 끝판왕입니다.",
            "불필요한 감정 소비 없이 객관적이고 정확한 솔루션을 제시합니다.",
            "깊이 있는 대화와 호기심을 나눌 수 있는 지적인 모범 단짝입니다."
        ],
        "match": "ENTJ (리자몽)"
    },
    "ENTJ": {
        "mbti_title": "대담한 통솔자 (ENTJ)",
        "ko_name": "리자몽",
        "en_name": "Charizard",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "types": [("불꽃", "#EE8130"), ("비행", "#A98FF3")],
        "features": "불타는 열정과 강한 비전을 지녔으며, 거침없는 추진력으로 앞장서 이끕니다.",
        "reason": [
            "어떤 어려운 난관도 정면으로 돌파해내는 당당한 카리스마가 있습니다.",
            "확확 트인 통찰력과 강한 책임감으로 목표를 반드시 달성해냅니다.",
            "당신이 주저할 때 자신감을 불어넣고 승리로 끌어줄 든든한 리더입니다."
        ],
        "match": "INTP (후딘)"
    },
    "ESFP": {
        "mbti_title": "자유로운 영혼의 연예인 (ESFP)",
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "types": [("노말", "#A8A878"), ("페어리", "#D685AD")],
        "features": "사랑스러운 사교성과 감흥을 몰고 다니며, 분위기를 단번에 즐겁게 만드는 분위기 메이커입니다.",
        "reason": [
            "솔직하고 솔직담백한 감정 표현으로 주변 사람들에게 웃음을 줍니다.",
            "순간의 즐거움을 만끽할 줄 아는 타고난 엔터테이너입니다.",
            "함께 있으면 심심할 틈 없이 매일이 축제처럼 신나는 단짝입니다."
        ],
        "match": "ISTJ (이상해꽃)"
    },
    "ISFP": {
        "mbti_title": "호기심 많은 예술가 (ISFP)",
        "ko_name": "잠만보",
        "en_name": "Snorlax",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "types": [("노말", "#A8A878")],
        "features": "여유롭고 온화하며, 자신만의 편안한 페이스로 세상을 관조하는 유쾌함을 가졌습니다.",
        "reason": [
            "남에게 피해 주는 것을 싫어하고 평화롭고 조용한 휴식을 애호합니다.",
            "부담 없이 편안하게 같이 마주앉아 있는 것만으로도 힐링을 줍니다.",
            "각박한 세상 속에서 당신에게 가장 따스한 안식처가 되어 줄 단짝입니다."
        ],
        "match": "ESTJ (거북왕)"
    },
    "ESTP": {
        "mbti_title": "모험을 즐기는 모험가 (ESTP)",
        "ko_name": "윈디",
        "en_name": "Arcanine",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "types": [("불꽃", "#EE8130")],
        "features": "바람처럼 빠른 순발력과 넘치는 순수 열정으로 행동부터 옮기는 순도 100% 실전파입니다.",
        "reason": [
            "복잡한 고민 대신 빠르게 다가가 직접 경험하는 화끈함이 특징입니다.",
            "위기의 순간에도 당황하지 않고 시원시원하게 상황을 해결해냅니다.",
            "스릴 넘치고 다이내믹한 순간을 함께 달리기에 이보다 완벽할 수 없습니다."
        ],
        "match": "ISFJ (메타몽)"
    },
    "ISTP": {
        "mbti_title": "만능 재주꾼 (ISTP)",
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "types": [("유령", "#70559B"), ("독", "#A040A0")],
        "features": "쿨하고 재치 넘치며, 필요한 상황에서 과묵하지만 확실한 실속을 챙기는 실용파입니다.",
        "reason": [
            "관찰력이 뛰어나며 불필요한 간섭 대신 유연하게 대응합니다.",
            "어떤 난관에 봉착해도 임기응변으로 재치 있게 헤쳐나갑니다.",
            "구속받지 않고 서로의 자유를 존중하면서도 최고로 재밌는 친구가 됩니다."
        ],
        "match": "ESFJ (해피너스)"
    },
    "ESTJ": {
        "mbti_title": "엄격한 관리자 (ESTJ)",
        "ko_name": "거북왕",
        "en_name": "Blastoise",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "types": [("물", "#6390F0")],
        "features": "체계적이고 단단하며, 굳건한 책임감과 남다른 해결 능력으로 신뢰감을 줍니다.",
        "reason": [
            "약속과 원칙을 철저히 지키며 어떤 일도 끝까지 빈틈없이 마칩니다.",
            "위기 상황일수록 단단한 방패처럼 팀과 친구를 지켜냅니다.",
            "흔들리지 않는 든든함으로 중심을 딱 잡아주는 확실한 수호자입니다."
        ],
        "match": "ISFP (잠만보)"
    },
    "ESFJ": {
        "mbti_title": "사교적인 친선도모형 (ESFJ)",
        "ko_name": "해피너스",
        "en_name": "Blissey",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "types": [("노말", "#A8A878")],
        "features": "세심한 다정함과 친절함으로 다친 마음과 몸을 정성껏 보살펴 주는 헌신파입니다.",
        "reason": [
            "상대방의 기분과 필요한 것을 기신같이 찾아내 챙겨줍니다.",
            "모두가 편안하고 행복하게 지낼 수 있도록 세심하게 배려합니다.",
            "언제나 온기 가득한 마음으로 마음을 어루만져 주는 따스한 단짝입니다."
        ],
        "match": "ISTP (팬텀)"
    },
    "ISTJ": {
        "mbti_title": "청렴결백한 논리주의자 (ISTJ)",
        "ko_name": "이상해꽃",
        "en_name": "Venusaur",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/3.png",
        "types": [("풀", "#7AC74C"), ("독", "#A040A0")],
        "features": "원칙을 지키고 묵묵히 제 자리를 지키며, 변함없는 묵직한 신뢰감을 전합니다.",
        "reason": [
            "요령 피우지 않고 본인이 맡은 바를 성실하게 해냅니다.",
            "시간이 흘러도 변함없이 곁에서 뿌리깊은 나무처럼 든든한 존재입니다.",
            "믿고 의지할 수 있는 진중하고 진실된 인생 단짝입니다."
        ],
        "match": "ESFP (푸린)"
    },
    "ISFJ": {
        "mbti_title": "용감한 수호자 (ISFJ)",
        "ko_name": "메타몽",
        "en_name": "Ditto",
        "img_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "types": [("노말", "#A8A878")],
        "features": "상대방의 성향과 마음에 스스로를 유연하게 맞춰주는 묵묵한 배려의 대명사입니다.",
        "reason": [
            "상대의 시선에서 깊이 이해하고 편안하게 맞춰줄 수 있습니다.",
            "드러나지 않아도 뒤에서 조용히 타인을 돕고 헌신합니다.",
            "나를 있는 그대로 받아들여 주는 세상에서 가장 포용력 넓은 단짝입니다."
        ],
        "match": "ESTP (윈디)"
    }
}

# 4. 헤더 영역 출력
st.markdown('<div class="main-title">⚡ MBTI x 포켓몬 단짝 찾기 🐾</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 성격 유형(MBTI)과 가장 잘 맞는 인생 포켓몬 단짝을 만나보세요!</div>', unsafe_allow_html=True)

# 5. MBTI 선택 셀렉트박스
mbti_options = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox(
    "👉 당신의 MBTI 유형을 선택해 주세요:",
    options=mbti_options,
    index=0,
    help="16가지 MBTI 중 하나를 고르면 단짝 포켓몬이 나타납니다."
)

# 6. 단짝 찾기 버튼 클릭 및 시각 효과 처리
if st.button("🎉 내 단짝 포켓몬 확인하기", use_container_width=True, type="primary"):
    # 축하 화면 효과 (폭죽/풍선 이벤트)
    st.balloons()
    
    data = POKEMON_DATA[selected_mbti]
    
    # 7. 카드 결과 출력
    st.markdown(f"### 💛 {selected_mbti} ({data['mbti_title'].split(' ')[1]}) 만의 단짝 포켓몬")
    
    with st.container():
        st.markdown('<div class="pokemon-card">', unsafe_allow_html=True)
        
        # 2열 레이아웃: 이미지(좌), 설명(우)
        col1, col2 = st.columns([1, 1.2])
        
        with col1:
            st.image(data["img_url"], use_container_width=True)
            
        with col2:
            st.markdown(
                f'<span class="pokemon-name-kr">{data["ko_name"]}</span>'
                f'<span class="pokemon-name-en">({data["en_name"]})</span>',
                unsafe_allow_html=True
            )
            
            # 타입 태그 생성
            types_html = ""
            for t_name, t_color in data["types"]:
                types_html += f'<span class="type-badge" style="background-color: {t_color};">{t_name}</span>'
            st.markdown(types_html, unsafe_allow_html=True)
            
            st.write(f"**✨ 성격 및 특징:** {data['features']}")

        # 이유 및 상세 설명
        reasons_html = "".join([f"<li>{r}</li>" for r in data["reason"]])
        st.markdown(
            f'''
            <div class="section-box">
                <div class="section-title">💡 왜 나랑 환상의 단짝일까?</div>
                <ul class="reason-list">
                    {reasons_html}
                </ul>
            </div>
            ''',
            unsafe_allow_html=True
        )

        # 최고 궁합 MBTI 안내
        st.markdown(
            f'<div class="chemistry-box">🤝 환상의 짝꿍 MBTI: <b>{data["match"]}</b></div>',
            unsafe_allow_html=True
        )
        
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # 최초 안내 문구
    st.info("💡 위의 MBTI를 고른 후 **[🎉 내 단짝 포켓몬 확인하기]** 버튼을 눌러보세요!")

# 8. 하단 카피라이트 안내
st.markdown("---")
st.caption("✨ 본 앱은 Streamlit으로 제작되었으며, 포켓몬 공식 이미지(PokeAPI CDN)를 활용합니다.")
