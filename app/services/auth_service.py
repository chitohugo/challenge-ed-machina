from datetime import timedelta

from app.core.config import configs
from app.core.exceptions import AuthError
from app.core.security import create_access_token, get_password_hash, verify_password
from app.model.lead import Lead
from app.repository.lead_repository import LeadRepository
from app.schema.auth_schema import Payload, SignIn, SignUp
from app.services.base_service import BaseService


class AuthService(BaseService):
    def __init__(self, lead_repository: LeadRepository):
        self.lead_repository = lead_repository
        super().__init__(lead_repository)

    def sign_in(self, sign_in: SignIn):
        lead: Lead = self.lead_repository.read_by_email(sign_in.email)
        if not lead:
            raise AuthError(detail="Incorrect email or password")

        if not verify_password(sign_in.password, lead.password):
            raise AuthError(detail="Incorrect password")

        payload = Payload(
            id=lead.id,
            email=lead.email,
            first_name=lead.first_name
        )
        token_lifespan = timedelta(minutes=configs.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token, expiration_datetime = create_access_token(payload.dict(), token_lifespan)
        response = {
            "access_token": access_token
        }
        return response

    def sign_up(self, sign_up: SignUp):
        lead = Lead(**sign_up.dict(exclude_none=True))
        lead.password = get_password_hash(sign_up.password)
        created_lead = self.lead_repository.create(lead)
        return created_lead
