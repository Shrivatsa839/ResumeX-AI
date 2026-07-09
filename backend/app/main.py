from fastapi import FastAPI

from app.api.health import router as health_router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Resume Analyzer & ATS Score Checker",
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ResumeX AI 🚀"
    }