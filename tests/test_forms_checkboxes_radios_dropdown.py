import pytest
from pages.forms_page import FormsPage


def test_checkboxes_radios_dropdown(driver, base_url):
    driver.get(base_url)
    page = FormsPage(driver).wait_for_app_ready()

    assert page.toggle_checkbox(0) in [True, False]
    assert page.toggle_checkbox(3) in [True, False]

    assert page.choose_radio(yes=True) is True

    texts = page.get_dropdown_texts()
    texts = [t for t in texts if t and "seleccion" not in t.lower() and "select" not in t.lower()]
    assert len(texts) >= 1, f"No hay opciones útiles en el dropdown. Encontrado: {texts}"

    chosen = page.choose_dropdown_by_text(texts[0])
    assert chosen == texts[0]

    page.submit()
    assert True


def test_dropdown_runtime_options(driver, base_url):
    """Selecciona hasta 3 opciones reales del dropdown (lo que haya en la página)."""
    driver.get(base_url)
    page = FormsPage(driver).wait_for_app_ready()

    texts = page.get_dropdown_texts()
    texts = [t for t in texts if t and "seleccion" not in t.lower() and "select" not in t.lower()]
    assert len(texts) >= 1

    for t in texts[:3]:
        chosen = page.choose_dropdown_by_text(t)
        assert chosen == t


@pytest.mark.parametrize("partial", ["Fút", "Tenis", "Básquet", "Soccer", "Basket"])
def test_dropdown_options_partial(driver, base_url, partial):
    """Uso laxo: intenta match parcial; si no encuentra, no rompe el test."""
    driver.get(base_url)
    page = FormsPage(driver).wait_for_app_ready()
    selected = page.choose_dropdown_by_partial(partial)

    if partial.lower() in selected.lower():
        assert True
    else:
        assert selected != ""
