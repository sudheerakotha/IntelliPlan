def generate_ai_insights(exams, subjects, topics):
    """
    Return simple recommendations based on data.
    """
    insights = []
    for exam in exams:
        insights.append(f"Start preparing for '{exam['name']}' early to avoid last-minute stress.")
        exam_subjects = subjects.get(exam['id'], [])
        total_topics = sum(len(topics.get(s['id'], [])) for s in exam_subjects)
        insights.append(f"'{exam['name']}' covers {total_topics} topics. Prioritize topics with high difficulty.")
    if not exams:
        insights.append("Add exams to get personalized study insights.")
    return insights
