import streamlit as st
from engine.recommender import AssessmentRecommender

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("🔍 SHL Assessment Recommendation Engine")

recommender = AssessmentRecommender("data/shl_catalog.csv")

skills = st.text_input("Required Skills (comma separated)").split(",")
job_level = st.selectbox("Job Level", ["Entry", "Mid", "Senior"])
industry = st.text_input("Industry", "Technology")
test_type = st.selectbox("Assessment Type", ["Technical", "Cognitive", "Behavioral"])
max_duration = st.slider("Maximum Duration (minutes)", 20, 90, 45)

if st.button("Recommend Assessments"):
    results = recommender.recommend(
        skills, job_level, industry, test_type, max_duration
    )

    for r in results[:5]:
        st.markdown(
            f"""
            <div style="padding:15px; border-radius:10px; background-color:#163d2d; margin-bottom:10px;">
                <h4>🧪 {r['name']}</h4>
                <p><b>Assessment ID:</b> {r['assessment_id']}</p>
                <p><b>Score:</b> {r['score']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        for reason in r["reasons"]:
            st.write(f"✔ {reason}")

