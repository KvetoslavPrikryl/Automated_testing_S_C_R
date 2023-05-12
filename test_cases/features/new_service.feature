@allure.feature
Feature: New srvice

Scenario: new service
Given I am logged in
When I click on button Hlavní stránka
And I click on přidat službu button
And I fill in form
And I click on save button
And I see new service
And I see price
And I delete new service
Then Log off
