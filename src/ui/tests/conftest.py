import pytest
from playwright.sync_api import sync_playwright
from src.ui.pages.pase_page import BasePage
from src.ui.pages.card_page import CartPage


@pytest.fixture(scope='function')
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel='chrome',headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()
    playwright.stop()

@pytest.fixture(scope='function')
def base_page(browser):
    return BasePage(browser)

@pytest.fixture(scope='function')
def cart_page(browser):
    return CartPage(browser)