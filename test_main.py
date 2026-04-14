from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_calculate_discount():
    # content to test
    payload = {"price": 200.0, "discount_percent" : 20.0}

    #call to get final discounted price
    response = client.post('/calculate_discount', json=payload)

    # Assert: Check the result
    assert response.status_code == 200
    assert response.json() == {"final_price": 160.0}
