from playwright.sync_api import expect
from pytest_bdd import scenarios, when, then, parsers

scenarios("features/cart.feature")


@when(parsers.parse('the user removes "{product}" from the cart'))
def remove_from_cart(inventory_page, product):
    inventory_page.remove_from_cart(product.lower().replace(" ", "-"))


@when("the user sorts products by price from low to high")
def sort_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")


@then(parsers.parse("the cart badge shows {count:d}"))
def badge_shows(inventory_page, count):
    expect(inventory_page.cart_badge).to_have_text(str(count))


@then("the cart badge is not shown")
def badge_hidden(inventory_page):
    expect(inventory_page.cart_badge).to_have_count(0)


@then(parsers.parse("the cart contains {count:d} items"))
def cart_contains(cart_page, count):
    expect(cart_page.items).to_have_count(count)


@then("the prices are in ascending order")
def prices_ascending(inventory_page):
    prices = inventory_page.price_values()
    assert prices == sorted(prices)
