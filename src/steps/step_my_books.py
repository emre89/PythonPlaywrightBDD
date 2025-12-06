from behave import given,when,then
from pages.my_books_page import MyBooksPage
from playwright.sync_api import sync_playwright

@given('"{book_title}" is in my books list')
def step_book_is_in_my_books_list(context, book_title):
    context.catalog_page.click_favorite_button_for_book_x_times(book_title, x=1)
    context.my_books_page.navigate_to_my_books_page()
    context.my_books_page.verify_my_favorite_book_list_has_book(book_title)
    
@when('I navigate to my books page')
def step_navigate_to_my_books_page(context):
    context.my_books_page.navigate_to_my_books_page()

@then('My books list should be empty')
def step_no_book_message_displayed(context):
    context.my_books_page.verify_my_favorite_book_list_is_empty()

@then('My books list should contain "{book_title}"')
def step_my_favorite_books_contain(context, book_title):
    context.my_books_page.verify_my_favorite_book_list_has_book(book_title)

@then('My books list should not contain "{book_title}"')
def step_my_favorite_books_do_not_contain(context, book_title):
    context.my_books_page.verify_my_favorite_book_list_has_not_book(book_title)