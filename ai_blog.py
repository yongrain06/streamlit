import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ✅ 클라우드에서도 작동하는 기본 폰트 설정
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 제목
st.title("🤖 인공지능 : AI 혁신의 물결")

# 소개
st.header("🌍 인공지능(AI)이란?")
st.markdown("""
**인공지능(AI)**은 인간처럼 학습하고 판단하며 문제를 해결할 수 있는 시스템입니다.  
챗봇, 자율주행, 의료 진단, 번역 기술 등 실생활 전반에서 활용되고 있습니다.
""")

# 기술
st.header("🧠 내가 사용하는 기술")
st.write("""
- Python, Streamlit, NumPy, Pandas, Matplotlib  
- OpenAI Codex, DALL·E  
- Google Gemini, Naver Clova
""")

# 주요 기업
st.header("🏢 주요 AI 기업 비교")
df = pd.DataFrame({
    "기업": ["OpenAI", "Google/DeepMind", "Naver"],
    "대표 모델": ["GPT-4, Codex", "Gemini, AlphaFold", "HyperCLOVA X, Clova"],
    "특징": [
        "생성형 AI 선도, GPT 시리즈",
        "멀티모달·로보틱스·단백질 구조 예측",
        "한국어 특화 LLM, 스마트 서비스"
    ]
})
st.write(df)

# 헬스케어 수용도
st.subheader("📊 AI 헬스케어 수용도")
st.markdown("출처: PwC 2024 Healthcare Consumer Insights Survey")
stats = {
    "18–34세 환자 AI 수용도 (%)": 80,
    "55세 이상 수용도 (%)": 60
}
fig1, ax1 = plt.subplots()
ax1.bar(stats.keys(), stats.values(), color=['#4CAF50', '#2196F3'])
ax1.set_ylim(0, 100)
ax1.set_ylabel("수용도 (%)")
ax1.set_title("연령대별 환자의 AI 진료 수용도")
for bar in ax1.patches:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{height}%", ha='center')
st.pyplot(fig1)

# 이미지 삽입
st.subheader("🖼️ AI 서버의 실제 모습")
st.image("ai_server.jpg", caption="UAE에 위치한 Microsoft 클라우드 데이터센터 내부 (출처: Microsoft)", use_container_width=True)

st.markdown("""
이 이미지는 아랍에미리트(UAE)에 위치한 Microsoft의 AI 전용 클라우드 데이터센터입니다.  
AI 모델들은 이런 고성능 서버에서 훈련되고, 실제 서비스를 위해 지속적으로 작동합니다.  
전 세계적으로 AI 기술이 발전할수록 이런 데이터센터의 중요성도 함께 커지고 있습니다.
""")

# 시장 전망
st.subheader("📈 AI 헬스케어 시장 성장 전망")
st.markdown("출처: Grand View Research, 2024")
st.markdown("""
AI는 의료 영상 분석, 음성 인식, 환자 데이터 분석 등 다양한 방식으로 의료 산업을 혁신하고 있어요.  
2024년 기준 265억 달러였던 시장 규모는 **2030년 1,877억 달러**로 성장할 전망입니다.
""")
years = [2024, 2030]
values = [26.57, 187.69]
fig2, ax2 = plt.subplots()
ax2.plot(years, values, marker='o', linestyle='-', color='#4CAF50')
ax2.set_title("AI 헬스케어 시장 성장 전망")
ax2.set_xlabel("연도")
ax2.set_ylabel("시장 규모 (십억 달러)")
for x, y in zip(years, values):
    ax2.text(x, y + 10, f"${y:.0f}B", ha='center')
ax2.set_ylim(0, max(values) + 50)
ax2.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig2)

# 사회적 과제
st.header("⚠️ AI의 사회적 과제")
st.markdown("""
- **개인정보 보호**: 민감한 의료·행정 데이터를 AI가 다루면서 프라이버시 위험 존재  
- **윤리와 신뢰성**: 편향된 데이터나 판단 책임 문제 발생 가능  
- **통제 불가능성**: 초거대 모델(GPT-4 등)이 예상치 못한 행동을 할 수 있음
""")

# 나의 목표
st.header("🎯 나의 진로 목표")
st.write("""
저는 AI 기술을 활용해 사회에 도움이 되는 현실적인 솔루션을 만들고 싶습니다.  
예: 의료 영상 분석, 학습 챗봇, 환경 시각화 시스템 등. 🚀
""")
st.text("AI를 통해 산업의 흐름을 최적화하고, 효율성을 끌어올리는 사람이 되고 싶습니다.")

# 참고자료
st.markdown("---")
st.subheader("📎 참고자료 및 링크")
st.markdown(
    "[Grand View Research](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-healthcare-market)  \n"
    "[PwC AI Consumer Survey](https://www.pwc.com/us/en/industries/health-industries/library/healthcare-consumer-insights-survey.html)  \n"
)
