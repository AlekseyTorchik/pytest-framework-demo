from pytest import mark


# Parametrization usage.
# Print different names of tv brands uses fixtures in conftest.py and source data file test_data.json
@mark.tv
def test_television_turns_on(tv_brand):
    print(f"\n {tv_brand} turns on as expected")


# Parametrization usage with build-in mark
@mark.tvp
@mark.parametrize('tv_brand', [('Samsung'), ('Sony'), ('Vizio')])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")


# Cross-browser testing
@mark.browsers
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('https://techstepacademy.com/training-ground')
