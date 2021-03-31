from pytest import fixture
from config import Config
from selenium import webdriver
import json

data_path = 'test_data.json'


# fixture for chrome browser thanks to that pages are open up in same browser window
@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    print('\n yield')


# Add custom option to pytest with comments. Type pytest -h and look at "custom options:"
def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment to run tests against")


# fixture for env configuration
@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


# fixture for create configuration from config.py
@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


# fixture for cross-browser testing
@fixture(params=[webdriver.Edge, webdriver.Chrome])
def browser(request):
    driver = request.param
    if driver == webdriver.Edge:
        drvr = driver(executable_path=r'D:\Programs\Setups\edgedriver64\msedgedriver.exe')
    else:
        drvr = driver()
    yield drvr
    drvr.quit()


# load tv brands from test_data.json for fixture
def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


# fixture for parametrized approach in test_television.py
@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
