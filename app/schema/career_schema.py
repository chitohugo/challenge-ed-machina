from typing import List

from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo


class BaseCareer(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class Career(ModelBaseInfo, BaseCareer):
    ...


class UpsertCareer(BaseCareer):
    ...


class FindCareerResult(BaseModel):
    careers: List[Career]
