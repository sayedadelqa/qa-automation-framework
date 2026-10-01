"""Steps shared by several feature files."""
from playwright.sync_api import expect
from pytest_bdd import given, when, then, parsers


@given("the user is on the login page")
def on_login_page(login_page):
    login_page.load()


@given("the user is logged in")
def user_logged_in(logged_in):
    """The `logged_in` fixture (root conftest) opens the site and logs in."""


@given(parsers.parse('the user adds "{product}" to the cart'))
@when(parsers.parse('the user adds "{product}" to the cart'))
def add_to_cart(inventory_page, product):
    inventory_page.add_to_cart(_slug(product))


@given("the user opens the cart")
@when("the user opens the cart")
def open_cart(inventory_page):
    inventory_page.open_cart()


def _slug(product_name: str) -> str:
    """'Sauce Labs Backpack' -> 'sauce-labs-backpack'"""
    return product_name.lower().replace(" ", "-")
