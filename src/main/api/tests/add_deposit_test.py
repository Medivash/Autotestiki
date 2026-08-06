import pytest

from src.main.api.model.add_deposit_request import AddDepositRequest
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.requests.add_deposit_requester import AddDepositRequester
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.create_user_requster import CreateUserRequester
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs


@pytest.mark.api
class TestAddDeposit:
    def test_add_deposit(self, api_manager, create_user_request):

        account = api_manager.user_steps.create_account(create_user_request)
        account_id = account.id
        add_deposit_request = AddDepositRequest(accountId=account_id, amount=1000)
        response = api_manager.user_steps.add_deposit(create_user_request, add_deposit_request)

        assert response.balance == 1000