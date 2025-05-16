from datetime import timedelta

def schedule_revisions(plan_df):
    revisions = []
    for _, row in plan_df.iterrows():
        for day_gap in [1, 2, 7]:  # spaced repetition pattern
            revision_date = row['Date'] + timedelta(days=day_gap)
            revisions.append({
                "Date": revision_date,
                "Topic": f"🔁 Revision: {row['Topic']}",
                "Hours": 1
            })
    return plan_df.append(revisions, ignore_index=True).sort_values(by="Date")
