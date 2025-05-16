def extract_topics_from_syllabus(syllabus_text):
    lines = syllabus_text.split("\n")
    topics = [line.strip() for line in lines if len(line.strip()) > 3]
    # Simple prioritization: sort by keyword weight
    priorities = sorted(topics, key=lambda x: x.count("*") + x.count("important"), reverse=True)
    return priorities if priorities else topics
