from src.main.api.model.base_model import BaseModel

class AddDepositResponse(BaseModel):
    id: int
    balance: float