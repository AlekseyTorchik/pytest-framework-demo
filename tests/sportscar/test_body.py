from pytest import mark


# Navigate to body page with fixture chrome_browser in conftest.py
@mark.ui
def test_can_navigate_to_body_page(chrome_browser):
    chrome_browser.get('https://www.motortrend.com/')
    assert True


# Body testing stub
@mark.smoke
@mark.body
class BodyTests:

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
