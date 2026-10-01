from pytest_bdd import scenarios, when, then, parsers

scenarios("features/products_api.feature")


@when(parsers.parse('I send a GET request to "{path}"'), target_fixture="response")
def send_get(api, path):
    return api.get(path)


@when(parsers.parse('I send a POST request to "{path}" with title "{title}"'), target_fixture="response")
def send_post(api, path, title):
    return api.post(path, {"title": title})


@then(parsers.parse("the response status is {status:d}"))
def status_is(response, status):
    assert response.status_code == status


@then(parsers.parse("the response contains {count:d} products"))
def contains_products(response, count):
    assert len(response.json()["products"]) == count


@then(parsers.parse('the response has the fields "{fields}"'))
def has_fields(response, fields):
    expected = {f.strip() for f in fields.split(",")}
    assert expected <= set(response.json())


@then(parsers.parse('the response title is "{title}"'))
def title_is(response, title):
    assert response.json()["title"] == title
