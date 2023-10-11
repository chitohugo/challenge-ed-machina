from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import and_, select
from sqlalchemy.orm import Session, joinedload
from fastapi_pagination.ext.sqlalchemy import paginate

from app.core.exceptions import RecordFound
from app.model.lead_career import LeadCareer
from app.model.lead import Lead
from app.repository.base_repository import BaseRepository
from app.schema.lead_career_schema import UpsertLeapCareer


class LeadCareerRepository(BaseRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        super().__init__(session_factory, LeadCareer)

    def read(self):
        with self.session_factory() as session:
            query = select(Lead).options(
                joinedload(Lead.careers).joinedload("subjects")
            )
            return paginate(session, query)

    def read_by_career(self, lead_id, career_id):
        with self.session_factory() as session:
            query = session.query(self.model)
            query = query.filter(and_(self.model.lead_id == lead_id, self.model.career_id == career_id)).first()
            if query:
                raise RecordFound(detail="Registration already exists")

    def create_with_career(self, schema: UpsertLeapCareer) -> None:
        with self.session_factory() as session:
            query = self.model(**schema.dict())
            session.add(query)
            session.commit()
            session.refresh(query)
