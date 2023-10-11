from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.career_subject_schema import CareerWithSubjects, UpsertCareerSubject, CareerSubject
from app.services.career_subject_service import CareerSubjectService

router = APIRouter(
    prefix="/career-subject",
    tags=["career_subject"],
    dependencies=[Depends(JWTBearer())]
)


@router.get("", response_model=List[CareerWithSubjects], dependencies=[Depends(get_current_user)])
@inject
async def get_careers_subjects(
        service: CareerSubjectService = Depends(Provide[Container.career_subject_service])
):
    careers_subjects = service.get_list()
    return careers_subjects


@router.get("/{career_subject_id}", response_model=CareerSubject, dependencies=[Depends(get_current_user)])
@inject
async def get_career_subject(
        career_subject_id: int,
        service: CareerSubjectService = Depends(Provide[Container.career_subject_service])
):
    return service.get_by_id(career_subject_id)


@router.post("", response_class=JSONResponse, dependencies=[Depends(get_current_user)])
@inject
async def create_career_subject(
        career_subject: UpsertCareerSubject,
        service: CareerSubjectService = Depends(Provide[Container.career_subject_service])
):
    service.add(career_subject)
    return {"message": "Successful registration"}


@router.patch("/{career_subject_id}", response_model=CareerSubject, dependencies=[Depends(get_current_user)])
@inject
async def update_career_subject(
        career_subject_id: int,
        career_subject: UpsertCareerSubject,
        service: CareerSubjectService = Depends(Provide[Container.career_subject_service])
):
    return service.patch(career_subject_id, career_subject)


@router.delete("/{career_subject_id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_career_subject(
        career_subject_id: int,
        service: CareerSubjectService = Depends(Provide[Container.career_subject_service])
):
    return service.remove_by_id(career_subject_id)
