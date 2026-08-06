from http import HTTPStatus

import requests

from src.main.api.model.credit_response import CreditResponse
from src.main.api.requests.requester import Requester
from src.main.api.model.credit_request import CreditRequest

class CreditRequester(Requester):
    def post(self, credit_request: CreditRequest):
        url=f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            json=credit_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.CREATED, HTTPStatus.OK]:
            return CreditResponse(**response.json())
        return response