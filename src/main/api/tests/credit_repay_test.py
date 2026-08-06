import pytest

from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.model.credit_repay_request import CreditRepayRequest
from src.main.api.model.credit_request import CreditRequest
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_user_requster import CreateUserRequester
from src.main.api.requests.credit_repay_requester import CreditRepayRequester
from src.main.api.requests.credit_requester import CreditRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestCreditRepay:
    def test_credit_repay(self, api_manager, create_credit_user_request):
        account = api_manager.user_steps.create_account(create_credit_user_request)
        account_id =  account.id
        credit_request = CreditRequest(accountId=account_id, amount=5000, termMonths=12)
        id = api_manager.user_steps.credit_request(create_credit_user_request, credit_request)
        credit_id = id.creditId
        credit_repay_request = CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=5000)
        response = api_manager.user_steps.credit_repay_request(create_credit_user_request, credit_repay_request)
        assert response.amountDeposited == 5000