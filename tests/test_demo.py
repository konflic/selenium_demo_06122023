

def test_main_page_title(browser):
    browser.get(browser.base_url)
    assert browser.title == "Your Store1"


def test_admin_page_title(browser, base_url):
    browser.get(f"{base_url}/admin")
    assert browser.title == "Administration"
