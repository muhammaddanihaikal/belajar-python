import pytest
from playwright.sync_api import sync_playwright
from config import BASE_URL

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(
        base_url=BASE_URL
    )
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()