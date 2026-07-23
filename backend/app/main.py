from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI Resume Analyzer & ATS Score Checker",
)

# ===========================
# API Routes
# ===========================

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)


# ===========================
# Root Endpoint
# ===========================

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to ResumeX AI 🚀"
    }