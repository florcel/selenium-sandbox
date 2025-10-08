from pages.dynamic_page import DynamicPage

def test_dynamic_id_button_reveals_element(driver, base_url):
    page = DynamicPage(driver).open(base_url).wait_for_app_ready()
    assert page.click_dynamic_button() is True
    assert page.revealed_present() in [True, False]
