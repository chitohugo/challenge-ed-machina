from sqlmodel import Field

from app.model.base_model import BaseModel


class LeadCareer(BaseModel, table=True):
    __tablename__ = "leads_careers"

    lead_id: int = Field(foreign_key="leads.id", nullable=False)
    career_id: int = Field(foreign_key="careers.id", nullable=False)

