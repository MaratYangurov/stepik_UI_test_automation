class TestBasePage:
    def test_monitors(self, base_page):
        base_page.open()
        base_page.switching_to_monitors()
        base_page.check_cards(number_of_cards=2)

    def test_transition_card(self, base_page):
        base_page.open()
        base_page.switching_to_card()
