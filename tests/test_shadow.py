from pages.shadow_page import ShadowPage

def test_shadow_dom(driver, base_url):
    page = ShadowPage(driver).open(base_url).wait_for_app_ready()
    txt = page.get_shadow_text()
    assert isinstance(txt, str) and len(txt) >= 1
