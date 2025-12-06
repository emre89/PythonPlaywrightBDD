Feature: Navigation between different pages
  As a user I should be able to see the relevant page content by navigating to different pages

  Background: 
    Given I visit the website

  Scenario: Verify navigation to catalog page
    When I navigate to catalog page
    Then I should see the header section
    And I should see "7" books in the catalog
    And Selected button should have text "Katalog"
  
  Scenario: Verify navigation to add book page
    When I navigate to add book page
    Then I should see the header section
    And I should see the add book form
    And Selected button should have text "Lägg till bok"

  Scenario: Verify navigation to my books page
    When I navigate to my books page
    Then I should see the header section
    And Selected button should have text "Mina böcker"
    And My books list should be empty

    


