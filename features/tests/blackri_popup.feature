# Created by carte at 9/2/2022
Feature: Tests initial homepage opening
  After the homepage is initially opened, popup menu will need to be handled

  Scenario: Verify user can interact with popup menu & proceed to homepage
    Given Open Home Page
    When Mouse hover on Main Menu items
    Then Print Main Menu links

