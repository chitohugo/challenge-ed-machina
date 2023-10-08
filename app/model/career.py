from sqlmodel import Field

from app.model.base_model import BaseModel


class Career(BaseModel, table=True):
    __tablename__ = "careers"

    name: str = Field(unique=True)
    description: str

