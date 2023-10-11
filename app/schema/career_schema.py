from typing import Optional, List

from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo
from app.schema.subject_schema import Subject


class BaseCareer(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class Career(ModelBaseInfo, BaseCareer):
    ...


class UpsertCareer(BaseCareer):
    ...


class GetCareerList(Career):
    subjects: Optional[List[Subject]]
    ...
