from pages.tables_page import TablesPage

def test_static_table_has_rows_and_messi(driver, base_url):
    page = TablesPage(driver).open(base_url).wait_for_app_ready()
    rows = page.static_rows()
    assert len(rows) >= 1
    assert page.static_has_messi() is True

def test_dynamic_table_has_rows(driver, base_url):
    page = TablesPage(driver).open(base_url).wait_for_app_ready()
    rows = page.dynamic_rows()
    assert len(rows) >= 1
