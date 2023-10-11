from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.core.config import configs
from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.lead_career_schema import LeadWithCareers, UpsertLeapCareer, LeadCareer
from app.services.lead_career_service import LeadCareerService

router = APIRouter(
    prefix="/lead-career",
    tags=["lead_career"],
    dependencies=[Depends(JWTBearer())]
)

Page = configs.Page

@router.get("", response_model=Page[LeadWithCareers], dependencies=[Depends(get_current_user)])
@inject
async def get_leads_careers(
        service: LeadCareerService = Depends(Provide[Container.lead_career_service])
):
    leads_careers = service.get_list()
    return leads_careers


@router.get("/{lead_career_id}", response_model=LeadCareer, dependencies=[Depends(get_current_user)])
@inject
async def get_lead_career(
        lead_career_id: int,
        service: LeadCareerService = Depends(Provide[Container.lead_career_service])
):
    return service.get_by_id(lead_career_id)


@router.post("", response_class=JSONResponse, dependencies=[Depends(get_current_user)])
@inject
async def create_lead_career(
        lead_career: UpsertLeapCareer,
        service: LeadCareerService = Depends(Provide[Container.lead_career_service])
):
    service.add(lead_career)
    return {"message": "Successful registration"}


@router.patch("/{lead_career_id}", response_model=LeadCareer, dependencies=[Depends(get_current_user)])
@inject
async def update_lead_career(
        lead_career_id: int,
        lead_career: UpsertLeapCareer,
        service: LeadCareerService = Depends(Provide[Container.lead_career_service])
):
    return service.patch(lead_career_id, lead_career)


@router.delete("/{lead_career_id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_lead_career(
        lead_career_id: int,
        service: LeadCareerService = Depends(Provide[Container.lead_career_service])
):
    return service.remove_by_id(lead_career_id)
