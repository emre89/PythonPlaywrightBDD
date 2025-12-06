from behave import when, then
from pages.catalog_page import CatalogPage
from playwright.sync_api import sync_playwright

@when('I navigate to catalog page')
def step_navigate_to_catalog_page(context):
    context.catalog_page.navigate_to_catalog_page()

@when('I click "{n}" th favorite button "{x}" times')
def step_click_nth_favorite_button_x_times(context,n,x):
    context.catalog_page.click_nth_favorite_button_x_times(n,x)

@then('I should see "{x}" books in the catalog')
def step_verify_book_count(context, x):
    context.catalog_page.verify_book_list_has_x_items(x)

@when('I click favorite button for the book "{book_title}"') 
def step_click_favorite_button_by_book_title(context,book_title):
    context.catalog_page.click_favorite_button_for_book_x_times(book_title, x=1)

@when('I click "{x}" times on favorite button for "{book_title}"') 
def step_click_favorite_button_by_book_title_x_times(context,book_title, x):
    context.catalog_page.click_favorite_button_for_book_x_times(book_title, x)

@then('"{book_title}" is displayed as "{favorite_or_infavorite}"')
def step_verify_favorite_status_of_book(context, book_title, favorite_or_infavorite):
    context.catalog_page.verify_favorite_status_of_book(book_title, favorite_or_infavorite)

@then('I should see the book "{title}" of author "{author}" in catalog')
def step_verify_book_is_in_catalog(context, title, author):
    context.catalog_page.verify_book_of_author_is_visible(title, author)

@then('Catalog should have the following books:')
def step_verify_catalog_items(context):
    expected = [row['item'] for row in context.table]
    actual = context.catalog_page.all_books.all_inner_texts()
    assert actual == expected, f"\nExpected: {expected}\nActual:   {actual}"
