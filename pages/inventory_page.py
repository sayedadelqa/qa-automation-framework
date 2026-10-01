from playwright.sync_api import Page
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.prices = page.locator("[data-test='inventory-item-price']")

    def add_to_cart(self, product_slug: str):
        """product_slug example: 'sauce-labs-backpack'"""
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def remove_from_cart(self, product_slug: str):
        self.page.locator(f"[data-test='remove-{product_slug}']").click()

    def sort_by(self, option_value: str):
        """option_value: az, za, lohi, hilo"""
        self.sort_dropdown.select_option(option_value)

    def price_values(self):
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def open_cart(self):
        self.cart_link.click()
