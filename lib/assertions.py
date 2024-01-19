import json
from requests import Response

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ пришел не в формате JSON. Текст ответа сервера: {response.text}'

        assert name in response_as_dict, f'JSON ответ не содержит ключа {name}'
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ пришел не в формате JSON. Текст ответа сервера: {response.text}'

        assert name in response_as_dict, f'JSON ответ не содержит ключа {name}'

    @staticmethod
    def assert_json_has_keys(response: Response, names):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ пришел не в формате JSON. Текст ответа сервера: {response.text}'

        for name in names:
           assert name in response_as_dict, f'JSON ответ не содержит ключа {name}'

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f'Ответ пришел не в формате JSON. Текст ответа сервера: {response.text}'

        assert name not in response_as_dict, f'JSON ответ содержит ключ {name}, но не должен.'

    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f'Неожиданный статус код в ответе сервера. Ожидаемый код {expected_status_code}. Фактический статус код {response.status_code}'
