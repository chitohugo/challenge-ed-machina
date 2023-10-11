from app.repository.career_repository import CareerRepository
from app.repository.career_subject_repository import CareerSubjectRepository
from app.repository.subject_repository import SubjectRepository
from app.schema.career_subject_schema import UpsertCareerSubject
from app.services.base_service import BaseService


class CareerSubjectService(BaseService):
    def __init__(self, career_subject_repository: CareerSubjectRepository, career_repository: CareerRepository,
                 subject_repository: SubjectRepository):
        self.career_subject_repository = career_subject_repository
        self.career_repository = career_repository
        self.subject_repository = subject_repository
        super().__init__(career_subject_repository)

    def add_with_subject(self, career_subject: UpsertCareerSubject):
        if career_subject:
            self.career_repository.read_by_id(career_subject.career_id)
            self.subject_repository.read_by_id(career_subject.subject_id)
            self.career_subject_repository.read_by_subject(career_subject.career_id, career_subject.subject_id)

            self.career_subject_repository.create_with_subject(career_subject)

    def get_list(self):
        return self.career_subject_repository.read()
