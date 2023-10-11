from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.career_schema import GetCareerList, Career, UpsertCareer
from app.services.career_service import CareerService

router = APIRouter(
    prefix="/career",
    tags=["career"],
    dependencies=[Depends(JWTBearer())]
)


@router.get("", response_model=List[GetCareerList], dependencies=[Depends(get_current_user)])
@inject
async def get_careers(
        service: CareerService = Depends(Provide[Container.career_service])
):
    careers = service.get_list()
    return careers


@router.get("/{career_id}", response_model=Career, dependencies=[Depends(get_current_user)])
@inject
async def get_career(
        career_id: int,
        service: CareerService = Depends(Provide[Container.career_service]),
):
    return service.get_by_id(career_id)


@router.post("", response_model=Career, dependencies=[Depends(get_current_user)])
@inject
async def create_career(
        career: UpsertCareer,
        service: CareerService = Depends(Provide[Container.career_service])
):
    return service.add(career)


@router.patch("/{career_id}", response_model=Career, dependencies=[Depends(get_current_user)])
@inject
async def update_career(
        career_id: int,
        career: UpsertCareer,
        service: CareerService = Depends(Provide[Container.career_service])
):
    return service.patch(career_id, career)


@router.delete("/{career_id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_career(
        career_id: int,
        service: CareerService = Depends(Provide[Container.career_service])
):
    return service.remove_by_id(career_id)
