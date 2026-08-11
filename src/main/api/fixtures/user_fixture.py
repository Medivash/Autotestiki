import random

import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_genrator import RandomModelGenerator
from src.main.api.model.create_user_credit_request import CreateUserCreditRequest
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.model.credit_repay_request import CreditRepayRequest
from src.main.api.model.credit_request import CreditRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_credit_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserCreditRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    response = api_manager.user_steps.create_account(user_request)
    return response

@pytest.fixture
def create_second_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def credit_repay_request(api_manager, credit_request, create_credit_user_request):
    credit = api_manager.user_steps.credit(credit_request, create_credit_user_request)
    return CreditRepayRequest(
        creditId = credit.creditId,
        accountId = credit_request.accountId,
        amount = 10000
    )

@pytest.fixture
def credit_request(api_manager, create_credit_user_request):
    account = api_manager.user_steps.create_account(create_credit_user_request)
    return CreditRequest(
        accountId=account.id,
        amount=10000,
        termMonths=12
    )