from behave import when, then, given
from pages.base_page import BasePage

@given('I visit the website')
def step_def_visit_website(context):
    context.base_page.go_to_home_page()

@then('I should see the header section')
def step_def_see_header_section(context):
    context.base_page.verify_header_section_loaded()
    
@then('Selected button should have text "{expected_text}"')
def step_def_verify_selected_nav_button(context, expected_text):
    context.base_page.verify_selected_button_has_text(expected_text)
    
