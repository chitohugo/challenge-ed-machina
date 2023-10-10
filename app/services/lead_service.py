from app.repository.career_repository import CareerRepository
from app.repository.lead_repository import LeadRepository
from app.schema.lead_schema import UpsertLeapCareer
from app.services.base_service import BaseService


class LeadService(BaseService):
    def __init__(self, lead_repository: LeadRepository, career_repository: CareerRepository):
        self.lead_repository = lead_repository
        self.career_repository = career_repository
        super().__init__(lead_repository)

    def add_whit_career(self, lead_career: UpsertLeapCareer):
        if lead_career:
            self.lead_repository.read_by_id(lead_career.lead_id)
            self.career_repository.read_by_id(lead_career.career_id)
            self.lead_repository.read_by_career(lead_career.lead_id, lead_career.career_id)

            self.lead_repository.create_with_career(lead_career)

    def get_list(self):
        return self.lead_repository.read()
