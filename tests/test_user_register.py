from datetime import datetime

import requests
import json
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    # def setup_method(self):
    #     base_part = "learnqa"
    #     domain = "example.com"
    #     random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    #     self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': self.email
        # }
        # response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        response = MyRequests.post("/user/", data=data)

        # assert response.status_code == 200, f'Неожиданный статус код {response.status_code} в ответе сервера'
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': email
        # }
        response = MyRequests.post("/user/", data=data)

        # assert response.status_code == 400, 'Неожиданный статус код в ответе сервера'
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists"

