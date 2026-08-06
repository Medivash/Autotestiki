from src.main.api.model.base_model import BaseModel

class CreateUserResponse(BaseModel):
    id: int
    username: str
    password: str
    role: str