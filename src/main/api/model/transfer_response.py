from src.main.api.model.base_model import BaseModel

class TransferResponse(BaseModel):
    fromAccountId: int
    toAccountId: int
    fromAccountIdBalance: float