from fastapi import FastAPI
from app.routers import user, subject, topic, schedule

app = FastAPI()

app.include_router(user.router)
app.include_router(subject.router)
app.include_router(topic.router)
app.include_router(schedule.router)

@app.get("/")
def root():
    return {"message": "Welcome to IntelliPlan API"}
