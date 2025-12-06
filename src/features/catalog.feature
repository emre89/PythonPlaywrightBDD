Feature: Catalog
    As a user
    I want to see a list of books
    So that I can choose my favorites
	
	Scenario: Catalog page
        Given I visit the website
        Then I should see the header section
        And Catalog should have the following books
			| item                                                                         |
			| ❤️"Hur man tappar bort sin TV-fjärr 10 gånger om dagen", Bertil Flimmer      |
			| ❤️"Kaffekokaren som visste för mycket", Saga Espresson                       |
			| ❤️"Min katt är min chef", Kattis Jamsson                                     |
			| ❤️"100 sätt att undvika måndagar", Göran Snooze                              |
			| ❤️"Gräv där du står – och hitta en pizzameny", Maja Skruv                    |
			| ❤️"Jag trodde det var tisdag", Kim Vilsen                                    |
			| ❤️"Att prata med växter – och vad de egentligen tycker om dig", Flora Tistel |