import uuid

from sqlmodel import Field

from app.model.base_model import BaseModel


class LeadCareer(BaseModel, table=True):
    __tablename__ = "leads_careers"

    lead_id: uuid.UUID = Field(foreign_key="leads.id", primary_key=True, index=True, nullable=False)
    career_id: uuid.UUID = Field(foreign_key="careers.id", primary_key=True, index=True, nullable=False)
