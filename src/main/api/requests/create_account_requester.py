import requests

from src.main.api.model.create_bank_account_response import CreateBankAccountResponse
from src.main.api.requests.requester import Requester


class CreateAccountRequester(Requester):
    def post(self, model=None) -> CreateBankAccountResponse:
        url=f"{self.base_url}/account/create"
        response = requests.post(
            url=url,
            headers=self.headers
        )
        self.response_spec(response)
        return CreateBankAccountResponse(**response.json())