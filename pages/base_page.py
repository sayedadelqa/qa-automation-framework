from playwright.sync_api import Page


class BasePage:
    """Shared behaviour for every page object."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/"):
        self.page.goto(path)
