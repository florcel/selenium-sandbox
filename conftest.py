# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url") if pytestconfig.getoption("--base-url", default=None) \
        else "https://thefreerangetester.github.io/sandbox-automation-testing/"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome|firefox")
    parser.addoption("--base-url", action="store", default=None, help="Base URL bajo prueba")

@pytest.fixture(scope="session")
def browser(pytestconfig):
    return pytestconfig.getoption("--browser").lower()

@pytest.fixture(scope="function")
def driver(browser):
    """Crea y destruye el WebDriver por test. Headless en CI, logs silenciosos."""
    devnull_file = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if os.getenv("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        options.add_argument("--window-size=1280,900")
        options.add_argument("--disable-notifications")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        service = ChromeService(ChromeDriverManager().install())
        try:
            devnull_file = open(os.devnull, "w")
            service.log_output = devnull_file  
        except Exception:
            pass

        drv = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager

        options = webdriver.FirefoxOptions()
        if os.getenv("CI"):
            options.add_argument("-headless")

        service = FirefoxService(GeckoDriverManager().install())
        try:
            devnull_file = open(os.devnull, "w")
            service.log_output = devnull_file
        except Exception:
            pass

        drv = webdriver.Firefox(service=service, options=options)
        drv.set_window_size(1280, 900)

    else:
        raise ValueError(f"Navegador no soportado: {browser}")

    try:
        yield drv
    finally:
        try:
            drv.quit()
        finally:
            if devnull_file:
                devnull_file.close()

import pytest as _pytest

@_pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "Reporte de Tests - Sandbox Automation"

def pytest_configure(config):
    pass
