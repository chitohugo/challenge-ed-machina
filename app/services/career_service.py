from app.repository.career_repository import CareerRepository
from app.services.base_service import BaseService


class CareerService(BaseService):
    def __init__(self, career_repository: CareerRepository):
        self.career_repository = career_repository
        super().__init__(career_repository)
        
    