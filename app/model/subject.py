from typing import Optional

from sqlmodel import Field, Relationship

from app.model.career_subject import CareerSubject
from app.model.career import Career
from app.model.base_model import BaseModel


class Subject(BaseModel, table=True):
    __tablename__ = "subjects"

    name: str = Field(unique=True)
    description: str

    careers: Optional[Career] = Relationship(back_populates="subjects", link_model=CareerSubject)
