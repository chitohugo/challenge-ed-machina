from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session, joinedload

from app.model.subject import Subject
from app.repository.base_repository import BaseRepository


class SubjectRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Subject)

    def read(self):
        with self.session_factory() as session:
            query = session.query(self.model)
            query = query.options(
                joinedload("careers")
            ).all()
            print(query)
            return query
