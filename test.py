from fastapi.testclient import TestClient
from api import router  # Change based on your actual FastAPI instance

client = TestClient(router)

def test_upload_orders():
    with open("test.csv", "rb") as file:
        response = client.post("/upload-orders/", files={"file": file})
    assert response.status_code == 200
