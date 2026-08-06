import pytest
from sqlalchemy.orm import Session
from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_genrator import RandomModelGenerator
from src.main.api.model.create_user_request import CreateUserRequest
from src.main.api.db.crud.user_crud import UserCrudDb as User



@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user_valid(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, "Пользователь создан, но не найден в бд"

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!sw0rd"),
            ("аб", "Pas!sw0rd"),
            ("абd!", "Pas!sw0rd"),
            ("Max23456", "Pas!sw0rд"),
            ("Max23456", "Pas!"),
            ("Max23457", "pas!sw0rd"),
            ("Max23457", "PAS!SW0RD"),
            ("Max23457", "PASSWA0SRD"),
            ("Max23457", "PASSWA!0SRD")
        ]
    )
    def test_create_user_invalid(self, db_session: Session, username: str, password: str, api_manager: ApiManager):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, "Пользователь создан, ошибка"