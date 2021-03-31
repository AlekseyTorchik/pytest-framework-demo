from pytest import mark


# Navigate to engine page with fixture chrome_browser in conftest.py
@mark.ui
@mark.engine
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('https://www.cosworth.com/case_studies/case-study-t-50/')
    assert True
