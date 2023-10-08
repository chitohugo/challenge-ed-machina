from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository.lead_repository import LeadRepository
from app.services.auth_service import AuthService
from app.services.lead_service import LeadService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.auth",
            "app.api.v1.endpoints.lead",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)

    lead_repository = providers.Factory(LeadRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, lead_repository=lead_repository)
    lead_service = providers.Factory(LeadService, lead_repository=lead_repository)
