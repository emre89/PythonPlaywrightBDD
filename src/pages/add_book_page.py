from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class AddBookPage(BasePage):
    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        
        self.title_input = page.get_by_test_id('add-input-title')
        self.author_input = page.get_by_test_id('add-input-author')
        self.submit_button = page.get_by_role('button', name=' Lägg till ny bok ')
    
    
    def verify_add_book_form_loaded(self):
        expect(self.submit_button).to_be_disabled()
        expect(self.submit_button).to_be_visible()
        expect(self.title_input).to_be_visible()
        expect(self.author_input).to_be_visible()


    def go_to_home_page(self):
        return super().go_to_home_page()
    
    def verify_header_section_loaded(self):
        return super().verify_header_section_loaded()
    
    def navigate_to_catalog_page(self):
        return super().navigate_to_catalog_page()
    
    def navigate_to_add_book_page(self):
        return super().navigate_to_add_book_page()
    
    def navigate_to_my_books_page(self):
        return super().navigate_to_my_books_page()
    
    def verify_selected_button_has_text(self, expected_text):
        return super().verify_selected_button_has_text(expected_text)