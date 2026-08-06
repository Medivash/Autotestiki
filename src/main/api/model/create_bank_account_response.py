from src.main.api.model.base_model import BaseModel

class CreateBankAccountResponse(BaseModel):
    id: int
    number: str
    balance: float