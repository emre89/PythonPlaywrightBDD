from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class MyBooksPage(BasePage):
    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        
        self.my_favorite_books = page.get_by_role('listitem')
        self.my_favorite_books_placeholder = page.locator('.favorites p')
    
    def verify_my_favorite_book_list_is_empty(self):
        expected_text = 'När du valt, kommer dina favoritböcker att visas här.'
        expect(self.my_favorite_books_placeholder).to_have_text(expected_text)
        expect(self.my_favorite_books).not_to_be_visible(timeout=100)
    
    
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