import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: 'ru' or 'es' or 'fr'")

@pytest.fixture(scope="function")
def languages(request):
    language = request.config.getoption("language")
    selected_language = None
    if language == "ru":
        print("\nstart for russian language")
        selected_language = "ru"
    elif language == "es":
        print("\nstart for spain language")
        selected_language = "es"
    elif language == "fr":
        print("\nstart for french language")
        selected_language = "fr"
    else:
        raise pytest.UsageError("--language should be 'ru' or 'es' or 'fr'")
    
    return selected_language
