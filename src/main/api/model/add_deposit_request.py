from src.main.api.model.base_model import BaseModel

class AddDepositRequest(BaseModel):
    accountId: int
    amount: float