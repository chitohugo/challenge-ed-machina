from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.lead import router as lead_router
from app.api.v1.endpoints.career import router as career_router
from app.api.v1.endpoints.subject import router as subject_router

routers = APIRouter()
router_list = [auth_router, lead_router, career_router, subject_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
