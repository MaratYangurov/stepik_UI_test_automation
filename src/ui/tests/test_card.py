

class TestCartPage:
    def test_card(self, cart_page):
        cart_page.open()
        cart_page.check_place_order_button()
