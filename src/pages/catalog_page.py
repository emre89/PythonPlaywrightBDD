from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        
        self.all_books = page.locator('.book')
        self.favorited_books = page.locator('.book').locator('xpath=//*[@class="star selected"]/parent::div').all
        self.favorite_buttons = page.locator('.star')
    
    def verify_book_list_has_x_items(self, x):
        expect(self.all_books).to_have_count(int(x))
    
    def click_nth_favorite_button_x_times(self, n, x):
        for t in range(x):
            self.favorite_buttons.nth(n).click()

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
