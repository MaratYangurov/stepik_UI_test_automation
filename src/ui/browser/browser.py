from playwright.sync_api import Cookie
from playwright.sync_api import Page


class Browser:
    """Класс для взаимодействия с методами браузера, а также вкладками и iframe"""
    def __init__(self, page: Page):
        self.page = page


    def do_to_url(self, url: str):
        """Переходит по указанному URL"""
        return self.page.goto(url)

    def reload_page(self):
        """Перезаписывает страницу"""
        return self.page.reload()

    def get_cookies(self):
        """Получает куки страницы"""
        return self.page.context.cookies()

    def add_cookie(self, cookies: Cookie):
        """Передаем список куков в хранилище браузера"""
        return self.page.context.add_cookies(cookies)

    def close_tab(self, number: int):
        """Закрывает страницу с указанным порядковым номером"""

        all_tabs = self.page.context.pages
        all_tabs[number].close()

    def switch_to_tab(self, number: int):
        """Переходит на страницу с указанным номером и закрывает предыдущие вкладки"""

        all_tabs = self.page.context.pages
        new_tab = all_tabs[number]
        new_tab.bring_to_front()
        new_tab.wait_for_load_state()
        return new_tab

    def switch_to_iframe_and_click(self, iframe_locator: str, locator_for_click: str):
        """Переходит на iframe и кликает по локатору в iframe"""
        frame = self.page.frame_locator(iframe_locator)
        frame.locator(locator_for_click).click()

    def alert_accept(self):
        """Принимает диалоговое окно и нажимает ОК"""

        self.page.on('dialog', lambda dialog: dialog.accept())

    def evalueate_javascript(self, script: str):
        """Выполняет javascript на странице"""
        return self.page.evaluate(script)

    def check_download_file(self):
        """Метод после действия которое вызывает загрузку файла, проверяет, что файл загрузился"""
        with self.page.expect_download() as download_info:
            download = download_info.value
            assert download.path() != ''

    def press_keys(self, keys: str):
        """Выполняет нажатие клавиш/сочетание клавиш на клаве"""
        self.page.keyboard.press(keys)