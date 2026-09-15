from src.ui.page_elements.base import Base


class Input(Base):
    """Предовтавляет методы для работы с полями ввода"""

    def fill(self, text: str, delay: int|float = None):
        """Метод для ввода текста"""
        if delay:
            self._element.type(text=text, delay=delay)
        else:
            self._element.fill(value=text)

    def clear(self):
        """Очищает поле ввода"""
        self._element.clear()
