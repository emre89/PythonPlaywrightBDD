Feature: Favorite books
	As a user 
	I should be able to add/remove books to/from my favorites list 
	So that I can update my favorite book list

	Background:
		Given I visit the website

	Scenario: Add a book to my favorites
		When I click favorite button for the book "Min katt är min chef"
		And I navigate to my books page
		Then My books list should contain "Min katt är min chef"

	Scenario: Remove a book from my favorites
		Given "Kaffekokaren som visste för mycket" is in my books list
		When I navigate to catalog page
		And I click favorite button for the book "Kaffekokaren som visste för mycket"
		Then My books list should not contain "Kaffekokaren som visste för mycket"

	Scenario Outline: Click favorite button multiple times
		When I click "<times>" times on favorite button for "<book>"
		Then "<book>" is displayed as "<favorite_or_infavorite>"

		Examples:
			| book                                               | times | favorite_or_infavorite |
			| Hur man tappar bort sin TV-fjärr 10 gånger om dagen | 3     | favorite               |
			| Min katt är min chef                                | 4     | infavorite             |
			| 100 sätt att undvika måndagar                       | 5     | favorite               |
			| Gräv där du står – och hitta en pizzameny           | 8     | infavorite             |