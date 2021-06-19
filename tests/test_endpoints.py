import json

from src.main import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_get_slide(client):
    response = client.post(
        "/get_slide",
        data=json.dumps(
            {"timestamp": 1221445323, "payload": "KL20-12031_B_2.35.1"}
        ),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["slide_id"] == "KL20-12031_B_2.35.1"
    assert data["accepted"]


def test_get_slides(client):
    response = client.post(
        "/get_slides",
        data=json.dumps(
            {
                "timestamp": 1221445323,
                "type": "ids",
                "payload": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"],
            }
        ),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["slide_ids"] == ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"]
    assert data["accepted"]


def test_store_slide(client):
    response = client.post(
        "/store_slide",
        data=json.dumps(
            {
                "timestamp": 1221445323,
                "payload": "KL20-12031_B_2.35.1",
                "storage_box": "box_1",
            }
        ),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["slide_id"] == "KL20-12031_B_2.35.1"
    assert not data["accepted"]


def test_store_slides(client):
    response = client.post(
        "/store_slides",
        data=json.dumps(
            {
                "timestamp": 12412354325,
                "storage_box": "box_1",
                "payload": ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"],
            }
        ),
        content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["slide_ids"] == ["KL20-12031_B_2.35.1", "KL20-11898_A_3.3.1"]
    assert not data["accepted"]
