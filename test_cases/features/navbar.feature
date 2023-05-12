@allure.feature
Feature: Navbar

Scenario: Navbar button
Given I am on the link
When I see title text
And I click on button
And I see title text on link
And I click on second button
And I see title text on link
And I click third button
Then I see the last title text on link


