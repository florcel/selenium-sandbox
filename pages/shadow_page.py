
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ShadowPage(BasePage):
    HOST = (By.ID, "shadow-host")

    def get_shadow_text(self):
        host = self.wait.until(lambda d: d.find_element(*self.HOST))
        shadow = self.driver.execute_script("return arguments[0].shadowRoot", host)
        p = shadow.find_element(By.CSS_SELECTOR, "p")
        return p.text.strip()
