from src.main.api.model.base_model import BaseModel

class CreditRepayResponse(BaseModel):
    creditId: int
    amountDeposited: float