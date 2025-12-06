import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CatalogPage(BasePage):
    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        
        self.all_books = page.locator('.book')
        self.favorited_books = page.locator('.book').locator('xpath=//*[@class="star selected"]/parent::div').all_inner_texts
        self.favorite_buttons = page.locator('.star')

    def get_book_by_title(self, book_title: str):
        return self.all_books.get_by_text(re.compile(fr'{re.escape(book_title)}'))

    def get_book_by_author(self, author: str):
        return self.all_books.get_by_text(re.compile(fr'{re.escape(author)}'))
    
    def get_favorite_button_by_book_title(self, book_title):
        return self.all_books.get_by_test_id(re.compile(fr"^star-.*{book_title.strip('"')}$"))
    
    def verify_favorite_status_of_book(self, book_title, favorite_or_infavorite):
        class_name = "star"
        if favorite_or_infavorite == "favorite":
            class_name += " selected"
        expect(self.get_favorite_button_by_book_title(book_title)).to_have_class(class_name) 

    def verify_book_list_has_x_items(self, x):
        expect(self.all_books).to_have_count(int(x))
        
    def verify_book_of_author_is_visible(self, title, author):
        expect(self.get_book_by_title(title)).to_be_visible()
        expect(self.get_book_by_author(author)).to_be_visible()
    
    def click_nth_favorite_button_x_times(self, n, x):
        for t in range(int(x)):
            self.favorite_buttons.nth(n).click(force=True)

    def click_favorite_button_for_book_x_times(self, title, x=1):
        for t in range(int(x)):
            self.get_favorite_button_by_book_title(title).click(force=True)

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
