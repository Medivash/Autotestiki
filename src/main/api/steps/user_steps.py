from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.model.add_deposit_request import AddDepositRequest
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.model.credit_repay_request import CreditRepayRequest
from src.main.api.model.credit_request import CreditRequest
from src.main.api.model.transfer_request import TransferRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_create()
        ).post()
        return response

    def add_deposit(self, create_user_request: CreateUserRequest, add_deposit_request: AddDepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ADD_DEPOSIT,
            ResponseSpecs.request_ok(),
        ).post(add_deposit_request)
        return response

    def transfer(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER,
            ResponseSpecs.request_ok(),
        ).post(transfer_request)
        return response

    def credit_request(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_create()
        ).post(credit_request)
        return response

    def credit_repay_request(self, create_user_request: CreateUserRequest, credit_repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY_REQUEST,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response