from playwright.sync_api import Page
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.items = page.locator("[data-test='inventory-item']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def checkout(self):
        self.checkout_button.click()
