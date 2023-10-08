import uuid

from sqlmodel import Field

from app.model.base_model import BaseModel


class Subject(BaseModel, table=True):
    __tablename__ = "subjects"

    name: str = Field(unique=True)
    description: str
    career_id: uuid.UUID = Field(foreign_key="careers.id", primary_key=True, index=True, nullable=False)
