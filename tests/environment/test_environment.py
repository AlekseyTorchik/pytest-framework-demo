from pytest import mark


# Test for "qa" and "dev" environments uses config.py and fixtures in conftest.py


# Test base url and port for "qa" environment
@mark.envtest
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80


# Test base url and port for "dev" environment
@mark.envtest
@mark.xfail(reason="Env was not DEV")
def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080


# Test base url and port for "staging" environment
@mark.envtest
@mark.skip(reason="Not a staging environment")
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'
