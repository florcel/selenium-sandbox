
from selenium.webdriver.common.by import By
from .base_page import BasePage

class TablesPage(BasePage):
    STATIC_TABLE = (By.XPATH, "//h2[contains(.,'Tabla estática')]/following::table[1]")
    DYNAMIC_TABLE = (By.XPATH, "//h2[contains(.,'Tabla dinámica')]/following::table[1]")

    def static_rows(self):
        table = self.wait.until(lambda d: d.find_element(*self.STATIC_TABLE))
        return table.find_elements(By.CSS_SELECTOR, "tbody tr")

    def dynamic_rows(self):
        table = self.wait.until(lambda d: d.find_element(*self.DYNAMIC_TABLE))
        return table.find_elements(By.CSS_SELECTOR, "tbody tr")

    def static_has_messi(self):
        table = self.wait.until(lambda d: d.find_element(*self.STATIC_TABLE))
        return "Messi" in table.text
