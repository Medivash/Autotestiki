from src.main.api.model.base_model import BaseModel

class CreditRepayRequest(BaseModel):
    creditId: int
    accountId: int
    amount: float