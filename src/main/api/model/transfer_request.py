from src.main.api.model.base_model import BaseModel

class TransferRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: float