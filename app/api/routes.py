from fastapi import APIRouter

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.lead import router as lead_router
from app.api.endpoints.career import router as career_router
from app.api.endpoints.subject import router as subject_router
from app.api.endpoints.lead_career import router as lead_career_router
from app.api.endpoints.career_subject import router as career_subject_router

routers = APIRouter()
router_list = [auth_router, lead_router, career_router, subject_router, lead_career_router, career_subject_router]

[routers.include_router(router) for router in router_list]
