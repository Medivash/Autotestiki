from src.main.api.model.base_model import BaseModel

class CreditResponse(BaseModel):
    id: int
    amount: float
    termMonths: int
    balance: float
    creditId: int