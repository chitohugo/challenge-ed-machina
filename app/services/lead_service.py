from app.repository.lead_repository import LeadRepository
from app.services.base_service import BaseService


class LeadService(BaseService):
    def __init__(self, lead_repository: LeadRepository):
        self.lead_repository = lead_repository
        super().__init__(lead_repository)