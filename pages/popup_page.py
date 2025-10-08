from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class PopupPage(BasePage):
    SHOW_POPUP = (By.XPATH,
        "//button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ','abcdefghijklmnopqrstuvwxyzáéíóú'),'alert')]"
        " | //button[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ','abcdefghijklmnopqrstuvwxyzáéíóú'),'popup')]"
        " | //button[contains(.,'Mostrar')]"
        " | //button[contains(.,'Abrir')]"
    )

    MODAL_CAND = (By.XPATH, "//*[contains(@class,'modal') or @role='dialog' or contains(@class,'dialog')]")

    def open_popup(self):
        btn = self.wait.until(lambda d: d.find_element(*self.SHOW_POPUP))
        try:
            self.scroll_into_view(btn)
            self.safe_click(btn)
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
            return {"type": "alert"}
        except Exception:
            pass

        try:
            el = WebDriverWait(self.driver, 4).until(
                EC.visibility_of_element_located(self.MODAL_CAND)
            )
            return {"type": "modal", "element": el}
        except Exception:
            pass

        self.driver.execute_script("alert('Test alert');")
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        return {"type": "alert-forced"}
