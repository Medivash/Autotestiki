from enum import Enum

from pydantic.v1.dataclasses import dataclass

from src.main.api.model.add_deposit_response import AddDepositResponse
from src.main.api.model.base_model import BaseModel
from typing import Optional, Type

from src.main.api.model.create_bank_account_response import CreateBankAccountResponse
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.model.create_user_response import CreateUserResponse
from src.main.api.model.credit_repay_request import CreditRepayRequest
from src.main.api.model.credit_repay_response import CreditRepayResponse
from src.main.api.model.credit_request import CreditRequest
from src.main.api.model.credit_response import CreditResponse
from src.main.api.model.login_user_request import LoginUserRequest
from src.main.api.model.login_user_response import LoginUserResponse
from src.main.api.model.transfer_response import TransferResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        url="/admin/create",
        response_model=CreateUserResponse
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        url="/admin/users",
        response_model=None
    )

    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        url="/auth/token/login",
        response_model=LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        request_model=None,
        url="/account/create",
        response_model=CreateBankAccountResponse
    )

    ADD_DEPOSIT= EndpointConfiguration(
        request_model=None,
        url="/account/deposit",
        response_model=AddDepositResponse
    )

    TRANSFER = EndpointConfiguration(
        request_model=None,
        url="/account/transfer",
        response_model=TransferResponse
    )

    CREDIT_REQUEST = EndpointConfiguration(
        request_model=None,
        url="/credit/request",
        response_model=CreditResponse
    )

    CREDIT_REPAY_REQUEST = EndpointConfiguration(
        request_model=None,
        url="/credit/repay",
        response_model=CreditRepayResponse
    )

    CREDIT_REPAY = EndpointConfiguration(
        request_model=CreditRepayRequest,
        url="/credit/repay",
        response_model=CreditRepayResponse
    )

    CREDIT = EndpointConfiguration(
        request_model=CreditRequest,
        url="/credit/request",
        response_model=CreditResponse
    )


