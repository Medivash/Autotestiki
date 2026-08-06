from http import HTTPStatus
import requests

from src.main.api.model.add_deposit_response import AddDepositResponse
from src.main.api.requests.requester import Requester
from src.main.api.model.add_deposit_request import AddDepositRequest

class AddDepositRequester(Requester):
    def post(self, add_deposit_request: AddDepositRequest):
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url=url,
            json=add_deposit_request.model_dump(),
            headers=self.headers
        )
        if response.status_code in [HTTPStatus.CREATED, HTTPStatus.OK]:
            return AddDepositResponse(**response.json())
        return response
