from contextlib import AbstractContextManager
from fastapi_pagination.ext.sqlalchemy import paginate
from typing import Callable

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.model.subject import Subject
from app.repository.base_repository import BaseRepository


class SubjectRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Subject)

    def read(self):
        with self.session_factory() as session:
            query = select(self.model).options(
                joinedload("careers")
            )
            return paginate(session, query)
