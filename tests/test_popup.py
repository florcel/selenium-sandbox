from pages.popup_page import PopupPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_popup_alert(driver, base_url):
    page = PopupPage(driver).open(base_url).wait_for_app_ready()
    result = page.open_popup()

    if result["type"].startswith("alert"):
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.accept()
        assert True
    else:
        assert result["element"].is_displayed()
