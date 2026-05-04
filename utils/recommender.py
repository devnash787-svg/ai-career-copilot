# Learning roadmap for each career

CAREER_ROADMAP = {
    "Data Scientist": [
        "Learn Python",
        "Learn Statistics",
        "Learn Machine Learning",
        "Practice Projects",
        "Learn SQL",
        "Build Portfolio"
    ],
    "Web Developer": [
        "Learn HTML & CSS",
        "Learn JavaScript",
        "Learn React",
        "Build Projects",
        "Deploy Websites"
    ],
    "Backend Developer": [
        "Learn Java/Python",
        "Learn APIs",
        "Learn Databases",
        "Build Backend Projects"
    ],
    "AI Engineer": [
        "Learn Python",
        "Learn Deep Learning",
        "Work on AI Projects",
        "Learn NLP/Computer Vision"
    ],
    "Data Analyst": [
        "Learn Excel",
        "Learn SQL",
        "Learn Data Visualization",
        "Use Power BI/Tableau"
    ]
}

def get_roadmap(career):
    return CAREER_ROADMAP.get(career, ["Start with basics", "Explore the field"])