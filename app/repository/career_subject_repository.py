from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload

from app.core.exceptions import RecordFound
from app.model.career import Career
from app.model.career_subject import CareerSubject
from app.repository.base_repository import BaseRepository
from app.schema.career_subject_schema import UpsertCareerSubject
from app.schema.lead_career_schema import UpsertLeapCareer


class CareerSubjectRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, CareerSubject)

    def read(self):
        with self.session_factory() as session:
            query = session.query(Career)
            query = query.options(
                joinedload("subjects")
            ).all()
            return query

    def read_by_subject(self, career_id, subject_id):
        with self.session_factory() as session:
            query = session.query(self.model)
            query = query.filter(and_(self.model.career_id == career_id, self.model.subject_id == subject_id)).first()
            if query:
                raise RecordFound(detail="Registration already exists")

    def create_with_subject(self, schema: UpsertCareerSubject) -> None:
        with self.session_factory() as session:
            query = CareerSubject(**schema.dict())
            session.add(query)
            session.commit()
            session.refresh(query)
