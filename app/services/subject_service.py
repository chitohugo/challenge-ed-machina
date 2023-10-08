from app.repository.subject_repository import SubjectRepository
from app.services.base_service import BaseService


class SubjectService(BaseService):
    def __init__(self, subject_repository: SubjectRepository):
        self.subject_repository = subject_repository
        super().__init__(subject_repository)
        
    