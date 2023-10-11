from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.config import configs
from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.lead_schema import UpsertLead, Lead
from app.services.lead_service import LeadService

router = APIRouter(
    prefix="/lead",
    tags=["lead"],
    dependencies=[Depends(JWTBearer())]
)

Page = configs.Page


@router.get("", response_model=Page[Lead], dependencies=[Depends(get_current_user)])
@inject
async def get_leads(
        service: LeadService = Depends(Provide[Container.lead_service])
):
    leads_careers = service.get_list()
    return leads_careers


@router.get("/{lead_id}", response_model=Lead, dependencies=[Depends(get_current_user)])
@inject
async def get_lead(
        lead_id: int,
        service: LeadService = Depends(Provide[Container.lead_service]),
):
    return service.get_by_id(lead_id)


@router.patch("/{lead_id}", response_model=Lead, dependencies=[Depends(get_current_user)])
@inject
async def update_lead(
        lead_id: int,
        lead: UpsertLead,
        service: LeadService = Depends(Provide[Container.lead_service])
):
    return service.patch(lead_id, lead)


@router.delete("/{lead_id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_lead(
        lead_id: int,
        service: LeadService = Depends(Provide[Container.lead_service])
):
    return service.remove_by_id(lead_id)
