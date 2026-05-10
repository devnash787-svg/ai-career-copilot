import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from utils.resume_parser import extract_skills
from utils.skill_gap import get_skill_gap
from utils.recommender import get_roadmap
from utils.chatbot import career_chatbot

# ================= LOAD CSS =================
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ================= LOAD DATASET =================
df = pd.read_csv("data/careers_dataset.csv")

X = df["skills"]
y = df["career"]

# ================= TRAIN MODEL =================
vectorizer = TfidfVectorizer()

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()

model.fit(X_vec, y)

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Career Copilot",
    layout="wide"
)

# ================= HEADER =================
st.markdown(
    "<h1 class='main-title'>🚀 AI Career Copilot</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>AI Powered Career Guidance Platform</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# ================= LAYOUT =================
col1, col2 = st.columns(2)

# ================= LEFT =================
with col1:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<h3 class='yellow'>✨ Enter Your Skills</h3>",
        unsafe_allow_html=True
    )

    skills_input = st.text_input(
        "",
        placeholder="python, machine learning, sql"
    )

    st.markdown(
        "<h3 class='green'>📄 Upload Resume</h3>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "",
        type=["txt"]
    )

    extracted_skills = []

    if uploaded_file:

        resume_text = uploaded_file.read().decode("utf-8")

        st.success("✅ Resume uploaded successfully")

        extracted_skills = extract_skills(resume_text)

        st.write("🧠 Extracted Skills:")
        st.write(extracted_skills)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT =================
with col2:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown(
        "<h3 class='blue'>📊 Career Analysis</h3>",
        unsafe_allow_html=True
    )

    if st.button("🚀 Analyze Career"):

        if uploaded_file:
            input_text = " ".join(extracted_skills)
            user_skills = extracted_skills

        else:
            input_text = skills_input
            user_skills = [
                s.strip().lower()
                for s in skills_input.split(",")
                if s.strip()
            ]

        if input_text:

            vec = vectorizer.transform([input_text])

            prediction = model.predict(vec)

            career = prediction[0]

            st.success(f"🎯 Predicted Career: {career}")

            st.session_state["career"] = career

            # Skill Gap
            missing_skills = get_skill_gap(user_skills, career)

            st.markdown("### 📉 Skill Gap")

            if missing_skills:
                for skill in missing_skills:
                    st.write(f"❌ {skill}")
            else:
                st.success("✅ No major skill gaps")

            # Roadmap
            st.markdown("### 📚 Learning Roadmap")

            roadmap = get_roadmap(career)

            for step in roadmap:
                st.write(f"👉 {step}")

        else:
            st.warning("⚠️ Please enter skills or upload resume")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= CHATBOT =================
st.markdown("---")

st.markdown(
    "<h3 class='blue'>🤖 Career Chatbot</h3>",
    unsafe_allow_html=True
)

user_query = st.text_input(
    "💬 Ask your career assistant",
    placeholder="Ask about salary, roadmap, skills..."
)

if "career" in st.session_state:

    if user_query:

        st.chat_message("user").write(user_query)

        response = career_chatbot(
            user_query,
            st.session_state["career"]
        )

        st.chat_message("assistant").write(response)

else:
    st.warning("⚠️ Analyze career first to activate chatbot")
