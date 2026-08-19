import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.model.add_deposit_request import AddDepositRequest
from src.main.api.model.create_user_request import CreateUserRequest


@pytest.mark.api
class TestAddDeposit:
    def test_add_deposit(self, api_manager: ApiManager, create_user_request: CreateUserRequest):

        account = api_manager.user_steps.create_account(create_user_request)
        account_id = account.id
        add_deposit_request = AddDepositRequest(accountId=account_id, amount=1000)
        response = api_manager.user_steps.add_deposit(create_user_request, add_deposit_request)

        assert response.balance == 1000

    def test_add_deposit_invalid(self, api_manager: ApiManager, create_user_request: CreateUserRequest):

        account = api_manager.user_steps.create_account(create_user_request)
        account_id = account.id
        add_deposit_request = AddDepositRequest(accountId=account_id, amount=10000)
        api_manager.user_steps.add_deposit_invalid(create_user_request, add_deposit_request)