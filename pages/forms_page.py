from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage


class FormsPage(BasePage):
    TEXT_INPUT = (By.ID, "formBasicText")
    CHECKBOXES = [(By.ID, f"checkbox-{i}") for i in range(5)] 
    RADIO_SI = (By.ID, "formRadio1")
    RADIO_NO = (By.ID, "formRadio2")
    SELECT = (By.ID, "formBasicSelect")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def _scroll_into_view(self, el):
        try:
            self.scroll_into_view(el)
        except Exception:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", el
            )

    def _safe_click(self, el):
        try:
            self.safe_click(el)
        except Exception:
            try:
                el.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", el)

    def fill_text(self, text: str):
        el = self.wait.until(lambda d: d.find_element(*self.TEXT_INPUT))
        self._scroll_into_view(el)
        el.clear()
        el.send_keys(text)
        return self

    def toggle_checkbox(self, index: int = 0):
        by, loc = self.CHECKBOXES[index]
        el = self.wait.until(lambda d: d.find_element(by, loc))
        self._scroll_into_view(el)
        self._safe_click(el)
        return el.is_selected()

    def choose_radio(self, yes: bool = True):
        target = self.RADIO_SI if yes else self.RADIO_NO
        el = self.wait.until(lambda d: d.find_element(*target))
        self._scroll_into_view(el)
        if not el.is_selected():
            self._safe_click(el)
        return el.is_selected()

    def get_dropdown_texts(self):
        """Devuelve la lista de textos visibles del select."""
        el = self.wait.until(lambda d: d.find_element(*self.SELECT))
        sel = Select(el)
        return [opt.text.strip() for opt in sel.options]

    def choose_dropdown_by_text(self, visible_text: str):
        """
        Intenta match EXACTO; si no existe, cae a 'contains' (case-insensitive).
        Si nada matchea, elige la primera opción real (salteando placeholder).
        """
        el = self.wait.until(lambda d: d.find_element(*self.SELECT))
        self._scroll_into_view(el)
        sel = Select(el)

        try:
            sel.select_by_visible_text(visible_text)
            return sel.first_selected_option.text
        except NoSuchElementException:
            pass

        wanted = visible_text.strip().lower()
        for opt in sel.options:
            if wanted in opt.text.strip().lower():
                opt.click()
                return opt.text

        if len(sel.options) > 1:
            sel.select_by_index(1)
        return sel.first_selected_option.text

    def choose_dropdown_by_partial(self, partial_text: str):
        """Selecciona la primera opción cuyo texto contenga 'partial_text'."""
        el = self.wait.until(lambda d: d.find_element(*self.SELECT))
        self._scroll_into_view(el)
        sel = Select(el)
        needle = partial_text.strip().lower()
        for opt in sel.options:
            if needle in opt.text.strip().lower():
                opt.click()
                return opt.text
        return sel.first_selected_option.text

    def submit(self):
        el = self.wait.until(lambda d: d.find_element(*self.SUBMIT))
        self._scroll_into_view(el)
        self._safe_click(el)
        return self
