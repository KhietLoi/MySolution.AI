from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_evaluate_translation():
    response = client.post(
        "/api/review/evaluate",
        json={
            "translation_id": "translation-001",
            "source_text": "Hello",
            "translated_text": "Xin chào",
            "source_language": "en",
            "target_language": "vi",
            "context": "General",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["translation_id"] == "translation-001"
    assert data["score"] == 95
    assert data["quality"] == "excellent"

def test_evaluate_batch():
    response = client.post(
        "/api/review/evaluate-batch",
        json={
            "items": [
                {
                    "translation_id": "translation-001",
                    "source_text": "Hello",
                    "translated_text": "Xin chào",
                    "source_language": "en",
                    "target_language": "vi",
                },
                {
                    "translation_id": "translation-002",
                    "source_text": "Save changes",
                    "translated_text": "Lưu thay đổi",
                    "source_language": "en",
                    "target_language": "vi",
                },
            ]
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["items"]) == 2

    assert data["items"][0]["translation_id"] == "translation-001"
    assert data["items"][1]["translation_id"] == "translation-002"