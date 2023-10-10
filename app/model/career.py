from typing import List

from sqlmodel import Field, Relationship

from app.model.career_subject import CareerSubject
from app.model.lead_career import LeadCareer
from app.model.base_model import BaseModel


class Career(BaseModel, table=True):
    __tablename__ = "careers"

    name: str = Field(unique=True)
    description: str

    subjects: List["Subject"] = Relationship(back_populates="careers", link_model=CareerSubject)
    leads: List["Lead"] = Relationship(back_populates="careers", link_model=LeadCareer)
