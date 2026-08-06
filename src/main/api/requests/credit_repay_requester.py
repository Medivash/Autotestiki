from http import HTTPStatus

import requests

from src.main.api.model.credit_repay_request import CreditRepayRequest
from src.main.api.model.credit_repay_response import CreditRepayResponse
from src.main.api.requests.requester import Requester

class CreditRepayRequester(Requester):
    def post(self, credit_repay_request: CreditRepayRequest):
        url=f"{self.base_url}/credit/repay"
        response = requests.post(
            url=url,
            json=credit_repay_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.CREATED, HTTPStatus.OK]:
            return CreditRepayResponse(**response.json())
        return response