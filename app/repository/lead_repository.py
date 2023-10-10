from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import and_
from sqlalchemy.orm import Session, joinedload

from app.core.exceptions import RecordFound
from app.model.lead_career import LeadCareer
from app.model.lead import Lead
from app.repository.base_repository import BaseRepository
from app.schema.lead_schema import UpsertLeapCareer


class LeadRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, Lead)

    def read_by_career(self, lead_id, career_id):
        with self.session_factory() as session:
            query = session.query(LeadCareer)
            query = query.filter(and_(LeadCareer.lead_id == lead_id, LeadCareer.career_id == career_id)).first()
            if query:
                raise RecordFound(detail="Registration already exists")

    def create_with_career(self, schema: UpsertLeapCareer) -> None:
        with self.session_factory() as session:
            query = LeadCareer(**schema.dict())
            session.add(query)
            session.commit()
            session.refresh(query)

    def read(self):
        with self.session_factory() as session:
            query = session.query(self.model)
            query = query.options(joinedload(self.model.careers).joinedload("subjects")).all()
            return query


