import pytest

@pytest.mark.smoketest
def test_hana_new(browser):
    browser.get("https://www.google.com")

    
