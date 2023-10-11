from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo
from app.schema.career_schema import Career
from app.schema.subject_schema import Subject


class BaseCareerSubject(BaseModel):
    career_id: int
    subject_id: int

    class Config:
        orm_mode = True


class CareerSubject(ModelBaseInfo, BaseCareerSubject):
    ...


class UpsertLead(BaseCareerSubject):
    ...


class GetLeadList(BaseCareerSubject):
    ...


class UpsertLeapCareer(BaseModel):
    lead_id: int
    career_id: int
    ...


class CareerWithSubjects(Career):
    subjects: Optional[List[Subject]]
    ...


class UpsertCareerSubject(BaseModel):
    career_id: int
    subject_id: int
    ...

