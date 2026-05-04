CAREER_SKILLS = {
    "Data Scientist": ["python", "machine learning", "data analysis", "statistics", "sql"],
    "Web Developer": ["html", "css", "javascript", "react"],
    "Backend Developer": ["java", "spring", "api", "sql"],
    "AI Engineer": ["python", "deep learning", "ai"],
    "Business Analyst": ["excel", "analysis", "communication"],
    "Software Engineer": ["c++", "algorithms", "problem solving"],
    "Data Analyst": ["sql", "powerbi", "data visualization"],
    "Cyber Security": ["network security", "linux"],
    "Full Stack Developer": ["react", "nodejs", "javascript"]
}

def get_skill_gap(user_skills, career):
    required_skills = CAREER_SKILLS.get(career, [])

    missing_skills = []

    for skill in required_skills:
        if skill not in user_skills:
            missing_skills.append(skill)

    return missing_skills