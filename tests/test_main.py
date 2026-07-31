
import pytest
from fastapi.testclient import TestClient

from src.main import app, store


@pytest.fixture(autouse=True)
def reset_store():
    """Clear in-memory data before every test so tests are independent."""
    store._expenses.clear()
    store._next_id = 1
    yield


client = TestClient(app)


def test_create_expense_returns_201_and_assigns_id():
    resp = client.post("/expenses", json={
        "title": "Groceries", "amount": 45.50, "category": "food", "date": "2026-07-01"
    })
    assert resp.status_code == 201
    body = resp.json()
    assert body["id"] == 1
    assert body["title"] == "Groceries"


def test_create_expense_rejects_negative_amount():
    resp = client.post("/expenses", json={
        "title": "Bad", "amount": -5, "category": "food", "date": "2026-07-01"
    })
    assert resp.status_code == 422  # FastAPI validation error


def test_create_expense_rejects_missing_field():
    resp = client.post("/expenses", json={"title": "Missing stuff"})
    assert resp.status_code == 422


def test_list_expenses_empty_initially():
    resp = client.get("/expenses")
    assert resp.status_code == 200
    assert resp.json() == []


def test_list_expenses_returns_all_added():
    client.post("/expenses", json={"title": "A", "amount": 10, "category": "food", "date": "2026-07-01"})
    client.post("/expenses", json={"title": "B", "amount": 20, "category": "travel", "date": "2026-07-02"})
    resp = client.get("/expenses")
    assert resp.status_code == 200
    assert len(resp.json()) == 2


def test_filter_by_category():
    client.post("/expenses", json={"title": "A", "amount": 10, "category": "food", "date": "2026-07-01"})
    client.post("/expenses", json={"title": "B", "amount": 20, "category": "travel", "date": "2026-07-02"})
    resp = client.get("/expenses", params={"category": "food"})
    assert resp.status_code == 200
    results = resp.json()
    assert len(results) == 1
    assert results[0]["title"] == "A"


def test_filter_by_category_is_case_insensitive():
    client.post("/expenses", json={"title": "A", "amount": 10, "category": "Food", "date": "2026-07-01"})
    resp = client.get("/expenses", params={"category": "food"})
    assert len(resp.json()) == 1


def test_totals_overall_and_by_category():
    client.post("/expenses", json={"title": "A", "amount": 10, "category": "food", "date": "2026-07-01"})
    client.post("/expenses", json={"title": "B", "amount": 20, "category": "food", "date": "2026-07-02"})
    client.post("/expenses", json={"title": "C", "amount": 5, "category": "travel", "date": "2026-07-03"})
    resp = client.get("/expenses/total")
    assert resp.status_code == 200
    body = resp.json()
    assert body["overall_total"] == 35
    by_cat = {c["category"]: c["total"] for c in body["by_category"]}
    assert by_cat["food"] == 30
    assert by_cat["travel"] == 5


def test_delete_expense_success():
    created = client.post("/expenses", json={
        "title": "A", "amount": 10, "category": "food", "date": "2026-07-01"
    }).json()
    resp = client.delete(f"/expenses/{created['id']}")
    assert resp.status_code == 204
    assert client.get("/expenses").json() == []


def test_delete_nonexistent_expense_returns_404():
    resp = client.delete("/expenses/999")
    assert resp.status_code == 404
