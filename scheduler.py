from datetime import datetime, timedelta
from collections import defaultdict

def generate_study_plan_with_topics(exams, subjects, topics):
    """
    Plan study sessions by distributing sessions weighted by
    topic priority and difficulty for each exam.
    
    exams: list of dicts with keys: id, name, exam_date
    subjects: dict {exam_id: [subjects]}
    topics: dict {subject_id: [topics]}
    
    Returns: dict {date: [session strings]}
    """

    plan = defaultdict(list)
    today = datetime.today().date()

    # For each exam, get days left
    for exam in exams:
        exam_date = datetime.strptime(exam['exam_date'], "%Y-%m-%d").date()
        days_left = (exam_date - today).days
        if days_left <= 0:
            continue

        # Collect all topics for this exam's subjects
        exam_subjects = subjects.get(exam['id'], [])
        all_topics = []
        for subj in exam_subjects:
            all_topics.extend(topics.get(subj['id'], []))

        if not all_topics:
            # fallback: generic study sessions
            for i in range(days_left):
                study_day = today + timedelta(days=i)
                plan[study_day].append(f"Review for {exam['name']}")
            continue

        # Calculate total weight for sessions (priority & difficulty)
        # Weight formula: priority (1 to 5, reversed) + difficulty (1 to 5)
        # priority 1 = highest priority, so weight = (6 - priority)
        weighted_topics = []
        total_weight = 0
        for t in all_topics:
            weight = (6 - t['priority']) + t['difficulty']  # e.g. priority 1, diff 5 -> 10
            weighted_topics.append((t, weight))
            total_weight += weight

        # Total study sessions = days_left * 1 (1 session per day)
        total_sessions = days_left

        # Assign sessions proportional to weight
        for t, weight in weighted_topics:
            num_sessions = max(1, int(total_sessions * weight / total_weight))
            # distribute sessions evenly across days_left
            interval = max(1, days_left // num_sessions)
            for s in range(num_sessions):
                day = today + timedelta(days=s*interval)
                if day >= exam_date:
                    day = exam_date - timedelta(days=1)
                plan[day].append(f"Study topic '{t['name']}' for exam '{exam['name']}'")

    return dict(plan)
