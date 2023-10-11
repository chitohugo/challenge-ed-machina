from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_user
from app.core.security import JWTBearer
from app.schema.base_schema import Blank
from app.schema.subject_schema import GetSubjectList, Subject, UpsertSubject
from app.services.subject_service import SubjectService

router = APIRouter(
    prefix="/subject",
    tags=["subject"],
    dependencies=[Depends(JWTBearer())]
)


@router.get("", response_model=List[GetSubjectList], dependencies=[Depends(get_current_user)])
@inject
async def get_subjects(
    service: SubjectService = Depends(Provide[Container.subject_service])
):
    subjects = service.get_list()
    return subjects


@router.get("/{subject_id}", response_model=Subject, dependencies=[Depends(get_current_user)])
@inject
async def get_subject(
    subject_id: int,
    service: SubjectService = Depends(Provide[Container.subject_service]),
):
    return service.get_by_id(subject_id)


@router.post("", response_model=Subject, dependencies=[Depends(get_current_user)])
@inject
async def create_subject(
    subject: UpsertSubject,
    service: SubjectService = Depends(Provide[Container.subject_service])
):
    return service.add(subject)


@router.patch("/{subject_id}", response_model=Subject, dependencies=[Depends(get_current_user)])
@inject
async def update_subject(
    subject_id: int,
    subject: UpsertSubject,
    service: SubjectService = Depends(Provide[Container.subject_service])
):
    return service.patch(subject_id, subject)


@router.delete("/{subject_id}", response_model=Blank, dependencies=[Depends(get_current_user)])
@inject
async def delete_subject(
    subject_id: int,
    service: SubjectService = Depends(Provide[Container.subject_service])
):
    return service.remove_by_id(subject_id)
