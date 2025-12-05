from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage
from pages.my_books_page import MyBooksPage

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    context.browser = context.browser_type.launch(headless=False)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"
    context.page.set_default_timeout(5000)

    context.base_page = BasePage(context.page, context.base_url)
    context.catalog_page = CatalogPage(context.page, context.base_url)
    context.add_book_page = AddBookPage(context.page, context.base_url)
    context.my_books_page = MyBooksPage(context.page, context.base_url)

def after_scenario(context, scenario):
    if context.page:
        context.page.close()

def after_all(context):
    if context.browser:
        context.browser.close()
