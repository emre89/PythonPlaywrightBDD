from behave import when, then
from pages.my_books_page import MyBooksPage
from playwright.sync_api import sync_playwright

@when('I navigate to my books page')
def step_navigate_to_my_books_page(context):
    context.my_books_page.navigate_to_my_books_page()

@then('My favorite books list should be empty')
def step_no_book_message_displayed(context):
    context.my_books_page.verify_my_favorite_book_list_is_empty()