from typing import Optional, List

from pydantic import BaseModel

from app.model.career import Career
from app.schema.base_schema import ModelBaseInfo


class BaseSubject(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class Subject(ModelBaseInfo, BaseSubject):
    ...


class UpsertSubject(BaseSubject):
    ...


class GetSubjectList(Subject):
    careers: Optional[List[Career]]
    ...
