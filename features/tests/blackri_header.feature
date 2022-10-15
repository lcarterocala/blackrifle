# Created by carte at 9/2/2022
Feature: Tests the header portion of the webpage
  All features of the header can be tested here

  Scenario: Verify user can interact with the header & cart is empty
    Given Open Home Page
    And Hover over main menu
    When Cart button is clicked
    Then Verify cart is empty

