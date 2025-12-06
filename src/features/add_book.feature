Feature: Favorite books
	As a user
	I want to add a new book to the catalog
	So that it is added to the end of the catalog

	Background:
		Given I visit the website
		Then I should see "7" books in the catalog

	Scenario: Add a new book
		When I navigate to add book page
		And I add a new book "Playwright is cool!" of author "Emre Erol"
		And I navigate to catalog page
		Then I should see the book "Playwright is cool!" of author "Emre Erol" in catalog
		And I should see "8" books in the catalog

	# Bug: user should not be able to create a duplicate book
	@skip  
	Scenario: Add a duplicate book
		When I navigate to add book page
		And I add a new book "Min katt är min chef" of author "Kattis Jamsson"
		And I navigate to catalog page
		Then I should see "7" books in the catalog
		And Catalog should have the following books
			| item                                                                         |
			| ❤️"Hur man tappar bort sin TV-fjärr 10 gånger om dagen", Bertil Flimmer      |
			| ❤️"Kaffekokaren som visste för mycket", Saga Espresson                       |
			| ❤️"Min katt är min chef", Kattis Jamsson                                     |
			| ❤️"100 sätt att undvika måndagar", Göran Snooze                              |
			| ❤️"Gräv där du står – och hitta en pizzameny", Maja Skruv                    |
			| ❤️"Jag trodde det var tisdag", Kim Vilsen                                    |
			| ❤️"Att prata med växter – och vad de egentligen tycker om dig", Flora Tistel |

	Scenario: Verify new book is displayed at the end of catalog
		When I navigate to add book page
		And I add a new book "Testautomatisering med python" of author "Test Testersson"
		And I navigate to catalog page
		Then Catalog should have the following books
			| item                                                                         |
			| ❤️"Hur man tappar bort sin TV-fjärr 10 gånger om dagen", Bertil Flimmer      |
			| ❤️"Kaffekokaren som visste för mycket", Saga Espresson                       |
			| ❤️"Min katt är min chef", Kattis Jamsson                                     |
			| ❤️"100 sätt att undvika måndagar", Göran Snooze                              |
			| ❤️"Gräv där du står – och hitta en pizzameny", Maja Skruv                    |
			| ❤️"Jag trodde det var tisdag", Kim Vilsen                                    |
			| ❤️"Att prata med växter – och vad de egentligen tycker om dig", Flora Tistel |
			| ❤️"Testautomatisering med python", Test Testersson                           |
