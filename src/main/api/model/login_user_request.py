from src.main.api.model.base_model import BaseModel


class LoginUserRequest(BaseModel):
    username: str
    password: str