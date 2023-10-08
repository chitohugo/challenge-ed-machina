from sqlmodel import Field

from app.model.base_model import BaseModel


class Lead(BaseModel, table=True):
    __tablename__ = "leads"

    email: str = Field(unique=True)
    username: str = Field(unique=True)
    first_name: str = Field(default=None, nullable=True)
    last_name: str = Field(default=None, nullable=True)
    password: str = Field()
