import pytest

from src.models.models import IprCalcRequest, IprCalcResponse

@pytest.fixture
def generate_data_for_tests():
    return {
        "input_data": IprCalcRequest(**{
            "p_res": 250,
            "wct": 50,
            "pi": 1,
            "pb": 150
        }),
        "expected_output": {
            "q_liq": [
                190.04, 187.46, 184.88, 182.12, 177.57, 171.27, 163.6,
                154.82, 145.13, 134.67, 123.54, 111.83, 99.60, 87.15,
                74.70, 62.25, 49.80, 37.35, 24.90, 12.45, 0
            ],
            "p_wf": [
                1.0, 13.45, 25.9, 38.35, 50.8, 63.25, 75.7, 88.15, 100.6,
                113.05, 125.5, 137.95, 150.4, 162.85, 175.3, 187.75,
                200.2, 212.65, 225.1, 237.55, 250.0
            ]
        }
    }


def test_calc_model_success(api_client, generate_data_for_tests):
    input_data = generate_data_for_tests['input_data']
    expected_data = generate_data_for_tests['expected_output']
    response = api_client.post("/ipr/calc", input_data.json(), json=IprCalcResponse).json()
    assert expected_data['q_liq'] == response['q_liq']
    assert expected_data['p_wf'] == response['p_wf']
