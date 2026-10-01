import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_get_products_list(api):
    response = api.get("/products", params={"limit": 5})
    body = response.json()
    assert response.status_code == 200
    assert len(body["products"]) == 5


@pytest.mark.regression
@pytest.mark.api
def test_get_single_product_fields(api):
    response = api.get("/products/1")
    body = response.json()
    assert response.status_code == 200
    assert body["id"] == 1
    assert {"id", "title", "price", "category"} <= set(body)


@pytest.mark.regression
@pytest.mark.api
def test_create_product(api):
    payload = {"title": "qa test product"}
    response = api.post("/products/add", payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


@pytest.mark.regression
@pytest.mark.api
def test_update_product(api):
    response = api.put("/products/1", {"title": "updated title"})
    assert response.status_code == 200
    assert response.json()["title"] == "updated title"


@pytest.mark.regression
@pytest.mark.api
def test_delete_product(api):
    response = api.delete("/products/1")
    assert response.status_code == 200
    assert response.json()["isDeleted"] is True


@pytest.mark.regression
@pytest.mark.api
def test_unknown_product_returns_404(api):
    assert api.get("/products/99999").status_code == 404
