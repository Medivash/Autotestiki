from http import HTTPStatus

import requests

from src.main.api.model.transfer_request import TransferRequest
from src.main.api.model.transfer_response import TransferResponse
from src.main.api.requests.requester import Requester


class TransferRequester(Requester):
    def post(self, add_deposit_request: TransferRequest):
        url = f"{self.base_url}/account/transfer"
        response = requests.post(
            url=url,
            json=add_deposit_request.model_dump(),
            headers=self.headers
        )
        if response.status_code in [HTTPStatus.CREATED, HTTPStatus.OK]:
            return TransferResponse(**response.json())
        return response