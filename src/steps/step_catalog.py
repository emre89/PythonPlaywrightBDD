from behave import when, then
from pages.catalog_page import CatalogPage
from playwright.sync_api import sync_playwright

@when('I navigate to catalog page')
def step_navigate_to_catalog_page(context):
    context.catalog_page.navigate_to_catalog_page()

@then('I should see "{x}" books in the list')
def step_verify_book_count(context, x):
    context.catalog_page.verify_book_list_has_x_items(x)