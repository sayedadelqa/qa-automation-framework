import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.ui
def test_add_item_updates_cart_badge(logged_in, inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.regression
@pytest.mark.ui
def test_remove_item_clears_cart_badge(logged_in, inventory_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.remove_from_cart("sauce-labs-backpack")
    expect(inventory_page.cart_badge).to_have_count(0)


@pytest.mark.regression
@pytest.mark.ui
def test_cart_shows_added_items(logged_in, inventory_page, cart_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.add_to_cart("sauce-labs-bike-light")
    inventory_page.open_cart()
    expect(cart_page.items).to_have_count(2)


@pytest.mark.regression
@pytest.mark.ui
def test_sort_price_low_to_high(logged_in, inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.price_values()
    assert prices == sorted(prices)
