from src.main.api.model.base_model import BaseModel

class User(BaseModel):
    username: str
    role: str

class LoginUserResponse(BaseModel):
    token: str
    user: User