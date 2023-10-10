from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo
from app.schema.career_schema import GetCareerList


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


class GetLeadList(Lead):
    ...


class UpsertLeapCareer(BaseModel):
    lead_id: int
    career_id: int
    ...


class LeadWithCareers(Lead):
    careers: Optional[List[GetCareerList]]
    ...
