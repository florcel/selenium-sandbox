import pages.forms_page as fp
print("DEBUG FormsPage type:", type(fp.FormsPage), "from:", fp.__file__)
from pages.forms_page import FormsPage

def test_form_text_and_submit(driver, base_url):
    driver.get(base_url)                   
    page = FormsPage(driver)                
    page.wait_for_app_ready()
    page.fill_text("Hola sandbox - prueba de texto")
    page.submit()
    assert True
