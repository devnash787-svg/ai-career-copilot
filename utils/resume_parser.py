import re

SKILLS_DB = [
    "python", "machine learning", "data analysis", "deep learning",
    "html", "css", "javascript", "react", "nodejs",
    "java", "spring", "sql", "excel", "powerbi",
    "c++", "algorithms", "linux", "network security"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            found_skills.append(skill)

    return list(set(found_skills))


