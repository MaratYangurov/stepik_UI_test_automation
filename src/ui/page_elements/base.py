from abc import ABC

from playwright.async_api import expect
from playwright.sync_api import Page

class Base(ABC):
    """Базовый класс для взаимодействия с элементами."""

    def __init__(
            self,
            page: Page,
            stratagy: str = None,
            selector: str = None,
            role = None,
            value: str = None
    ):
        self.page = page
        self.stratagy = stratagy
        self.selector = selector
        self.role = role
        self.value = value

        if stratagy == 'locator':
            self._element = self.page.locator(self.selector)
        elif stratagy == 'by_role':
            self._element = self.page.get_by_role(role=self.role, name=self.value)
        elif stratagy == 'by_text':
            self._element = self.page.get_by_text(text=self.value)
        elif stratagy == 'by_placeholder':
            self._element = self.page.get_by_placeholder(text=self.value)
        else:
            raise ValueError('Указана неверная стратегия')

    def click(self):
        """Кликает по элементу"""
        self._element.click()

    def check_visible(self, visible=True):
        """Проверяет видимость Элемента
        :param visible: видимость элемента"""
        expect(self._element).to_be_visible(visible=True)

    def wait_for(self, state, timeout_msec: int= None):
        """Ожидает, когда _element удовлетворяет условию state"""
        self._element.wait_for(state=state, timeout=timeout_msec)
        

