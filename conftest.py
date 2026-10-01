"""Shared fixtures. pytest-playwright already provides the `page` fixture."""
import pytest
from api.api_client import ApiClient
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import load_json


@pytest.fixture(scope="session")
def users():
    return load_json("users.json")


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def logged_in(login_page, users):
    """Open the site and log in with the valid user."""
    login_page.load()
    login_page.login(**users["valid"])


@pytest.fixture(scope="session")
def api():
    return ApiClient()
