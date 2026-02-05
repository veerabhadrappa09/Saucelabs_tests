
import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options


# ---------- Custom CLI option ----------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome | firefox | edge"
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser").lower()


# ---------- WebDriver setup ----------
@pytest.fixture
def setup(browser):
    options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


# ---------- Pytest HTML metadata ----------
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Ecommerce Saucelabs"
    config.stash[metadata_key]["Test Module Name"] = "Admin Login tests"
    config.stash[metadata_key]["Tester Name"] = "Veera"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
