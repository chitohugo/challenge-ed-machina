from datetime import datetime
from typing import List, Optional, Union
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ModelBaseInfo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime
    updated_at: datetime


class FindBase(BaseModel):
    ordering: Optional[str]
    page: Optional[int]
    page_size: Optional[Union[int, str]]


class SearchOptions(FindBase):
    total_count: Optional[int]


class FindResult(BaseModel):
    founds: Optional[List]
    search_options: Optional[SearchOptions]


class Blank(BaseModel):
    pass
