from playwright.sync_api import Page, expect
from src.ui.pages.pase_page import BasePage
from src.ui.helper.urls import BASE_URL, CART_URL


class CartPage(BasePage):
    """Логика для тестов на странице корзина."""

    def __init__(self, page: Page, url=BASE_URL+CART_URL):
        super().__init__(page, url)

    def check_place_order_button(self):
        element = self.page.get_by_role(role='button', name='Place Order')
        expect(element).to_be_visible(visible=True)