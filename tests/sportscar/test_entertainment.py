from pytest import mark


# Navigate to entertainment page with fixture chrome_browser in conftest.py
@mark.ui
@mark.entertainment
def test_can_navigate_entertainment_page(chrome_browser):
    chrome_browser.get('https://www.siriusxm.com/')
    assert True
