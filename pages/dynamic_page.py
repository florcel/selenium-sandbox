from selenium.webdriver.common.by import By
from .base_page import BasePage

class DynamicPage(BasePage):
    BUTTON_BY_TEXT = (By.XPATH, "//button[contains(.,'Hacé click para generar un ID dinámico')]")
    REVEALED_ANY = (By.XPATH, "//*[contains(.,'oculto') or contains(.,'mostrado')]")

    def click_dynamic_button(self):
        self.wait.until(lambda d: d.find_element(*self.BUTTON_BY_TEXT)).click()
        return True

    def revealed_present(self):
        try:
            self.wait.until(lambda d: d.find_element(*self.REVEALED_ANY))
            return True
        except Exception:
            return False
