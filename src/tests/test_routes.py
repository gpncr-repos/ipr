import numpy as np
import pytest


@pytest.fixture
def generate_data_for_tests():
    return {
                "p_res": 250,
                "wct": 50,
                "pi": 1,
                "pb": 150,
            }


def test_calc_model_success(api_client, generate_data_for_tests):
    response = api_client.post("ipr/calc",
                               json=generate_data_for_tests)
    assert response.status_code == 200
    result = response.json()
    assert result
    assert result["p_wf"]
    assert result["q_liq"]
