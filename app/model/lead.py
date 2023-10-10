from typing import List

from sqlmodel import Field, Relationship

from app.model.lead_career import LeadCareer
from app.model.base_model import BaseModel


class Lead(BaseModel, table=True):
    __tablename__ = "leads"

    email: str = Field(unique=True)
    username: str = Field(unique=True)
    first_name: str = Field(default=None, nullable=True)
    last_name: str = Field(default=None, nullable=True)
    password: str = Field()

    careers: List["Career"] = Relationship(back_populates="leads", link_model=LeadCareer)
