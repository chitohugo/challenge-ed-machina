from typing import List

from pydantic import BaseModel

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


class FindSubjectResult(BaseModel):
    subjects: List[Subject]
