import pytest
import requests

from src.main.api.classes.api_manager import ApiManager
from src.main.api.model.create_user_credit_request import CreateUserCreditRequest
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.model.credit_request import CreditRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_user_requster import CreateUserRequester
from src.main.api.requests.credit_requester import CreditRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestCreditRequest:
    def test_credit_request(self, api_manager: ApiManager, create_credit_user_request: CreateUserCreditRequest):
        account = api_manager.user_steps.create_account(create_credit_user_request)
        account_id =  account.id
        credit_request = CreditRequest(accountId=account_id, amount=5000, termMonths=12)
        response = api_manager.user_steps.credit_request(create_credit_user_request, credit_request)
        assert  response.amount == 5000


    def test_credit_request_invalid(self, api_manager: ApiManager, create_credit_user_request: CreateUserCreditRequest):
        account = api_manager.user_steps.create_account(create_credit_user_request)
        account_id =  account.id
        credit_request = CreditRequest(accountId=account_id, amount=16000, termMonths=12)
        api_manager.user_steps.credit_request_invalid(create_credit_user_request, credit_request)