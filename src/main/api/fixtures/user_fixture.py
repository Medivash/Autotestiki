import pytest

from src.main.api.generators.model_genrator import RandomModelGenerator
from src.main.api.model.create_user_credit_request import CreateUserCreditRequest
from src.main.api.model.create_user_request import CreateUserRequest


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