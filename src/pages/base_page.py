from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

        # Common elements
        self.image_header = page.get_by_role("heading", name=" Läslistan ")
        self.background_image = page.get_by_alt_text("Bokklubb på café")
        self.page_header = page.get_by_role('heading', name=' Välkommen! ')
        self.page_description = page.get_by_role('heading', name=' Sidan för dig som gillar att läsa. Välj dina favoriter. ')

        # Navigation buttons
        self.catalog_button = page.get_by_role("navigation").get_by_test_id("catalog")
        self.add_book_button = page.get_by_role("navigation").get_by_test_id("add-book")
        self.my_books_button = page.get_by_role("navigation").get_by_test_id("favorites")
        self.selected_button = page.get_by_role("navigation").get_by_role('button', disabled=True)


    def go_to_home_page(self):
        self.page.goto(self.base_url)

    def navigate_to_catalog_page(self):
        if (self.catalog_button.is_disabled):
            print('You are already on the catalog page')
        else:
            self.catalog_button.click()

    def navigate_to_my_books_page(self):
        self.my_books_button.click()

    def navigate_to_add_book_page(self):
        self.add_book_button.click()
    
    def verify_header_section_loaded(self):
        expect(self.background_image).to_be_visible()
        expect(self.image_header).to_be_visible()
        expect(self.catalog_button).to_be_visible()
        expect(self.add_book_button).to_be_visible()
        expect(self.my_books_button).to_be_visible()

    def verify_selected_button_has_text(self, expected_text):
        expect(self.selected_button).to_have_text(expected_text)
        