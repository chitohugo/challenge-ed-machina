from app.repository.career_repository import CareerRepository
from app.repository.lead_career_repository import LeadCareerRepository
from app.repository.lead_repository import LeadRepository
from app.schema.lead_career_schema import UpsertLeapCareer
from app.services.base_service import BaseService


class LeadCareerService(BaseService):
    def __init__(self, lead_career_repository: LeadCareerRepository, lead_repository: LeadRepository,
                 career_repository: CareerRepository):
        self.lead_career_repository = lead_career_repository
        self.lead_repository = lead_repository
        self.career_repository = career_repository
        super().__init__(lead_career_repository)

    def add(self, lead_career: UpsertLeapCareer):
        if lead_career:
            self.lead_repository.read_by_id(lead_career.lead_id)
            self.career_repository.read_by_id(lead_career.career_id)

            self.lead_career_repository.read_by_career(lead_career.lead_id, lead_career.career_id)
            self.lead_career_repository.create_with_career(lead_career)

    def get_list(self):
        return self.lead_career_repository.read()
