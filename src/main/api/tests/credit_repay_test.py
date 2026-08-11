import pytest

from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.model.create_user_credit_request import CreateUserCreditRequest
from src.main.api.model.credit_repay_request import CreditRepayRequest
from src.main.api.model.credit_request import CreditRequest
from src.main.api.requests.credit_repay_requester import CreditRepayRequester
from src.main.api.db.crud.user_crud import UserCrudDb as User
from src.main.api.db.crud.credit_crud import  CreditCrudDb as Credit


@pytest.mark.api
class TestCreditRepay:
    def test_credit_repay(self, api_manager: ApiManager, create_credit_user_request: CreateUserCreditRequest):
        account = api_manager.user_steps.create_account(create_credit_user_request)
        account_id =  account.id
        credit_request = CreditRequest(accountId=account_id, amount=5000, termMonths=12)
        id = api_manager.user_steps.credit_request(create_credit_user_request, credit_request)
        credit_id = id.creditId
        credit_repay_request = CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=5000)
        response = api_manager.user_steps.credit_repay_request(create_credit_user_request, credit_repay_request)
        assert response.amountDeposited == 5000

    def test_credit_repay_new(self, api_manager: ApiManager, credit_repay_request: CreditRepayRequester, create_credit_user_request: CreateUserCreditRequest, db_session: Session):

        response = api_manager.user_steps.credit_repay(credit_repay_request, create_credit_user_request)
        assert credit_repay_request.creditId == response.creditId, "Проверка совпадает"

        credit_from_db = Credit.get_credit_account_by_id(db_session, response.creditId)
        assert credit_from_db.id == response.creditId

    def test_credit_repay_invalid(self, api_manager: ApiManager, create_credit_user_request: CreateUserCreditRequest):
        account = api_manager.user_steps.create_account(create_credit_user_request)
        account_id =  account.id
        credit_request = CreditRequest(accountId=account_id, amount=5000, termMonths=12)
        id = api_manager.user_steps.credit_request(create_credit_user_request, credit_request)
        credit_id = id.creditId
        credit_repay_request = CreditRepayRequest(creditId=credit_id, accountId=account_id, amount=6000)
        api_manager.user_steps.credit_repay_request_invalid(create_credit_user_request, credit_repay_request)