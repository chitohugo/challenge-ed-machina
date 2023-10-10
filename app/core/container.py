from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository.career_repository import CareerRepository
from app.repository.lead_repository import LeadRepository
from app.repository.subject_repository import SubjectRepository
from app.services.auth_service import AuthService
from app.services.career_service import CareerService
from app.services.lead_service import LeadService
from app.services.subject_service import SubjectService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.auth",
            "app.api.v1.endpoints.lead",
            "app.api.v1.endpoints.career",
            "app.api.v1.endpoints.subject",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    lead_repository = providers.Factory(LeadRepository, session_factory=db.provided.session)
    career_repository = providers.Factory(CareerRepository, session_factory=db.provided.session)
    subject_repository = providers.Factory(SubjectRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, lead_repository=lead_repository)
    lead_service = providers.Factory(LeadService, lead_repository=lead_repository, career_repository=career_repository)
    career_service = providers.Factory(CareerService, career_repository=career_repository, subject_repository=subject_repository)
    subject_service = providers.Factory(SubjectService, subject_repository=subject_repository)
