from typing import List

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo


class BaseLead(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BaseLeadWithPassword(BaseLead):
    password: str


class Lead(ModelBaseInfo, BaseLead):
    ...


class FindLead(FindBase, BaseLead):
    email: str
    ...


class UpsertLead(BaseLead):
    ...


class FindLeadResult(BaseModel):
    leads: List[Lead]
