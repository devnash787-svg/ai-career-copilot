import streamlit as st
import pickle
import plotly.express as px

from utils.resume_parser import extract_skills
from utils.skill_gap import get_skill_gap
from utils.recommender import get_roadmap
from utils.chatbot import career_chatbot

# Load CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load model
model = pickle.load(open("models/career_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="AI Career Copilot", layout="wide")

# Header
st.markdown("<h1 class='main-title'>🚀 AI Career Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-powered Career Guidance System</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout
col1, col2 = st.columns(2)

# ================= LEFT =================
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<h3 class='yellow'>✨ Enter Your Skills</h3>", unsafe_allow_html=True)
    skills_input = st.text_input("", placeholder="python, machine learning, sql")

    st.markdown("<h3 class='green'>📄 Upload Resume</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["txt"])

    resume_text = ""
    extracted_skills = []

    if uploaded_file:
        resume_text = uploaded_file.read().decode("utf-8")
        st.success("✅ Resume uploaded successfully")

        extracted_skills = extract_skills(resume_text)
        st.write("🧠 Extracted Skills:", extracted_skills)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT =================
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("<h3 class='blue'>📊 Analysis</h3>", unsafe_allow_html=True)

    if st.button("🚀 Analyze Career"):

        if uploaded_file:
            input_text = " ".join(extracted_skills)
            user_skills = extracted_skills
        else:
            input_text = skills_input
            user_skills = [s.strip().lower() for s in skills_input.split(",")]

        if input_text:

            vec = vectorizer.transform([input_text])
            career = model.predict(vec)[0]

            st.success(f"🎯 Predicted Career: {career}")

            # Skill gap
            missing_skills = get_skill_gap(user_skills, career)

            st.markdown("### 📉 Skill Gap")
            st.write(missing_skills if missing_skills else "✅ No gaps")

            # Plotly Chart
            st.markdown("### 📊 Skill Analysis")

            fig = px.bar(
                x=["Your Skills", "Missing Skills"],
                y=[len(user_skills), len(missing_skills)],
                title="Skill Comparison",
                labels={"x": "Category", "y": "Count"}
            )
            st.plotly_chart(fig, use_container_width=True)

            # Roadmap
            st.markdown("### 📚 Roadmap")
            roadmap = get_roadmap(career)
            for step in roadmap:
                st.write("👉", step)

            st.session_state["career"] = career

        else:
            st.warning("⚠️ Enter skills or upload resume")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= CHATBOT =================
st.markdown("---")
st.markdown("<h3 class='blue'>🤖 Career Chatbot</h3>", unsafe_allow_html=True)

user_query = st.text_input("💬 Ask your career assistant", placeholder="skills, salary, roadmap?")

if "career" in st.session_state:
    if user_query:
        st.chat_message("user").write(user_query)
        response = career_chatbot(user_query, st.session_state["career"])
        st.chat_message("assistant").write(response)
else:
    st.warning("Analyze career first to activate chatbot")
