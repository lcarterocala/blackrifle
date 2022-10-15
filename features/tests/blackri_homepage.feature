# Created by carte at 10/14/2022
Feature:  Tests the homepages primary functions
  All features of the homepage are tested here

  Scenario: Testing the arrows and hover effect for coffee bag images
    Given Open Home Page
    When Scroll down to working area
    Then Interact with the coffee bag image arrows
    Then Hover over coffee bag images

  Scenario: Testing the slider knob
    Given Open Home Page
    When Scroll down to working area
    Then Move the slider knob to the left and right

