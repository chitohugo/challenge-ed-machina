from pydantic import BaseModel

from app.schema.base_schema import ModelBaseInfo


class BaseLead(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class BaseLeadWithPassword(BaseLead):
    password: str


class Lead(ModelBaseInfo, BaseLead):
    ...


class UpsertLead(BaseLead):
    ...
