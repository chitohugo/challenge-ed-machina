from sqlmodel import Field

from app.model.base_model import BaseModel


class CareerSubject(BaseModel, table=True):
    __tablename__ = "careers_subjects"

    career_id: int = Field(foreign_key="careers.id", nullable=False)
    subject_id: int = Field(foreign_key="subjects.id", nullable=False)

