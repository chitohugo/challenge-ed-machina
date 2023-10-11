from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository.career_repository import CareerRepository
from app.repository.career_subject_repository import CareerSubjectRepository
from app.repository.lead_career_repository import LeadCareerRepository
from app.repository.lead_repository import LeadRepository
from app.repository.subject_repository import SubjectRepository
from app.services.auth_service import AuthService
from app.services.career_service import CareerService
from app.services.career_subject_service import CareerSubjectService
from app.services.lead_career_service import LeadCareerService
from app.services.lead_service import LeadService
from app.services.subject_service import SubjectService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.endpoints.auth",
            "app.api.endpoints.lead",
            "app.api.endpoints.career",
            "app.api.endpoints.subject",
            "app.api.endpoints.lead_career",
            "app.api.endpoints.career_subject",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    lead_repository = providers.Factory(LeadRepository, session_factory=db.provided.session)
    career_repository = providers.Factory(CareerRepository, session_factory=db.provided.session)
    subject_repository = providers.Factory(SubjectRepository, session_factory=db.provided.session)
    lead_career_repository = providers.Factory(LeadCareerRepository, session_factory=db.provided.session)
    career_subject_repository = providers.Factory(CareerSubjectRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, lead_repository=lead_repository)
    lead_service = providers.Factory(LeadService, lead_repository=lead_repository)
    career_service = providers.Factory(CareerService, career_repository=career_repository,
                                       subject_repository=subject_repository)
    subject_service = providers.Factory(SubjectService, subject_repository=subject_repository)
    lead_career_service = providers.Factory(LeadCareerService, lead_career_repository=lead_career_repository,
                                            lead_repository=lead_repository, career_repository=career_repository)
    career_subject_service = providers.Factory(CareerSubjectService,
                                               career_subject_repository=career_subject_repository,
                                               career_repository=career_repository,
                                               subject_repository=subject_repository)
