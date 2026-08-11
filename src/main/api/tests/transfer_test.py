import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.model.add_deposit_request import AddDepositRequest
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.model.transfer_request import TransferRequest


@pytest.mark.api
class TestTransfer:
    def test_transfer(self, api_manager: ApiManager, create_user_request: CreateUserRequest, create_second_user_request: CreateUserRequest):

        account = api_manager.user_steps.create_account(create_user_request)
        account_id = account.id
        add_deposit_request = AddDepositRequest(accountId=account_id, amount=1001)
        api_manager.user_steps.add_deposit(create_user_request, add_deposit_request)
        account = api_manager.user_steps.create_account(create_second_user_request)
        second_account = account.id
        transfer_request = TransferRequest(fromAccountId=account_id, toAccountId=second_account, amount=1000.0)
        response = api_manager.user_steps.transfer(create_user_request, transfer_request)

        assert response.fromAccountIdBalance == 1

    def test_transfer_invalid(self, api_manager, create_user_request, create_second_user_request):

        account = api_manager.user_steps.create_account(create_user_request)
        account_id = account.id
        add_deposit_request = AddDepositRequest(accountId=account_id, amount=1001)
        api_manager.user_steps.add_deposit(create_user_request, add_deposit_request)
        account = api_manager.user_steps.create_account(create_second_user_request)
        second_account = account.id
        transfer_request = TransferRequest(fromAccountId=account_id, toAccountId=second_account, amount=5000.0)
        api_manager.user_steps.transfer_invalid(create_user_request, transfer_request)