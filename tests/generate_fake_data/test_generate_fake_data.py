import json

import pytest

from src.generate_fake_data.main import FakeGenerate


class TestGenerateFakeData():

    @pytest.fixture
    def fake_data_result(self):
        fake_generator = FakeGenerate()
        result = fake_generator.generate_data_fake()
        return json.loads(result)

    def test_return_type(self, fake_data_result):
        # Verifica se o resultado é um dicionário
        assert isinstance(fake_data_result, dict)

    def test_keys_present(self, fake_data_result):
        # Verifica se as chaves esperadas estão no dicionário
        expected_keys = ['user_fake', 'name_fake', 'sex_fake', 'address_fake', 'email_fake', 'birthdate_fake']
        for key in expected_keys:
            assert key in fake_data_result

    def test_non_empty_values(self, fake_data_result):
        # Verifica se os valores para as chaves não são vazios
        for key in fake_data_result:
            assert fake_data_result[key]