import pytest
import requests

class TestFirstAPI:
    names = [
        ('Kateryna'),
        ('Maria'),
        ('')
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}
        response = requests.get(url, params=data)

        assert response.status_code == 200, 'Статус код не соответсвует ожидаемому'

        response_dict = response.json()
        assert "answer" in response_dict, 'В ответе сервера нет поля "answer"'

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert expected_response_text == actual_response_text, 'Полученный текст приветствия не совпадает с ождидаемым'