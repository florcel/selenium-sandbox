from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

DEFAULT_TIMEOUT = 20

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        return self

    def wait_for_app_ready(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.wait.until(lambda d: d.execute_script(
            "var r=document.querySelector('#root'); return !!(r && r.children && r.children.length>0);"
        ) is True)
        return self

    def scroll_into_view(self, el):
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el)

    def safe_click(self, el):
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)
