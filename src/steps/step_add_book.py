from behave import when, then
from pages.add_book_page import AddBookPage
from playwright.sync_api import sync_playwright

@when('I navigate to add book page')
def step_navigate_to_add_book_page(context):
    context.add_book_page.navigate_to_add_book_page()

@then('I should see the add book form')
def step_verify_add_book_form_loaded(context):
    context.add_book_page.verify_add_book_form_loaded()

@when('I add a new book "{title}" of author "{author}"')
def step_add_book(context, title, author):
    context.add_book_page.add_book(title,author)