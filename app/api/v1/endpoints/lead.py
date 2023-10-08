from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.lead_schema import FindLeadResult, UpsertLead, Lead
from app.services.lead_service import LeadService

router = APIRouter(
    prefix="/lead",
    tags=["lead"],
    dependencies=[Depends(JWTBearer())]
)


@router.get("", response_model=FindLeadResult, dependencies=[Depends(get_current_user)])
@inject
async def get_leads(
    service: LeadService = Depends(Provide[Container.lead_service])
):
    leads = service.get_list()
    return {"leads": leads}


@router.get("/{lead_id}", response_model=Lead, dependencies=[Depends(get_current_user)])
@inject
async def get_lead(
    lead_id: int,
    service: LeadService = Depends(Provide[Container.lead_service]),
):
    return service.get_by_id(lead_id)


@router.post("", response_model=Lead, dependencies=[Depends(get_current_user)])
@inject
async def create_lead(
    lead: UpsertLead,
    service: LeadService = Depends(Provide[Container.lead_service])
):
    return service.add(lead)


@router.patch("/{lead_id}", response_model=Lead, dependencies=[Depends(get_current_user)])
@inject
async def update_lead(
    user_id: int,
    lead: UpsertLead,
    service: LeadService = Depends(Provide[Container.lead_service])
):
    return service.patch(user_id, lead)


@router.delete("/{lead_id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_lead(
    lead_id: int,
    service: LeadService = Depends(Provide[Container.lead_service])
):
    return service.remove_by_id(lead_id)
