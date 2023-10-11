from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo
from app.schema.career_schema import GetCareerList
from app.schema.lead_schema import Lead


class BaseLeadCareer(BaseModel):
    lead_id: int
    career_id: int

    class Config:
        orm_mode = True


class LeadCareer(ModelBaseInfo, BaseLeadCareer):
    ...


class UpsertLead(BaseLeadCareer):
    ...


class GetLeadList(LeadCareer):
    ...


class UpsertLeapCareer(BaseModel):
    lead_id: int
    career_id: int
    ...


class LeadWithCareers(Lead):
    careers: Optional[List[GetCareerList]]
    ...
