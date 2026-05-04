def career_chatbot(user_input, career):
    
    user_input = user_input.lower()

    if "skill" in user_input:
        return f"For {career}, focus on improving your core technical skills."

    elif "job" in user_input:
        return f"You can apply for entry-level {career} roles or internships."

    elif "roadmap" in user_input:
        return f"Follow the roadmap shown above step-by-step."

    elif "salary" in user_input:
        return f"{career} salaries depend on skills, but grow fast with experience."

    else:
        return "Ask about skills, jobs, roadmap, or salary 😊"