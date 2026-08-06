from src.main.api.model.base_model import BaseModel

class CreditRequest(BaseModel):
    accountId: int
    amount: float
    termMonths: int
