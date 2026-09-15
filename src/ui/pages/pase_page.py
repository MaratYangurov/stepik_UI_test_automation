from playwright.sync_api import Page

from src.ui.helper.urls import BASE_URL, CART_URL


class BasePage:
    """Логика для тестов на главной странице."""

    def __init__(self, page: Page, url=BASE_URL):
        self.page = page
        self.url = url

    def open(self):
        """Открываем страницу по url"""
        return self.page.goto(self.url)

    def switching_to_monitors(self):
        """Кликает на мониторы"""
        self.page.get_by_text(text='Monitors').click()
        self.page.get_by_text(text='Apple monitor 24').wait_for(state='visible')

    def check_cards(self, number_of_cards: int):
        """Проверяет кол-во карточек с товаром
        :param number_of_cards: количество карточек с товаром"""
        monitors = self.page.locator('.card-block')
        cnt = monitors.count()
        assert cnt == number_of_cards

    def switching_to_card(self):
        """Кликает на мониторы"""
        self.page.locator('#cartur').click()
        assert CART_URL in self.page.url
