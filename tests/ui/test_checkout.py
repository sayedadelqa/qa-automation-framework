import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.ui
def test_complete_purchase(logged_in, inventory_page, cart_page, checkout_page, users):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_info(**users["checkout_info"])
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


@pytest.mark.regression
@pytest.mark.ui
def test_checkout_requires_first_name(logged_in, inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_info("", "Adel", "12345")
    expect(checkout_page.error).to_contain_text("First Name is required")
