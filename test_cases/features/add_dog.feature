@allure.feature
Feature: Add dog

Scenario: Add dog
Given I am logged in
When I click on button Hlavní stránka
And I click on button Přidat psa
And I fill in form
And I click on button Uložit
And I click on button Štěňata
And I see this new dog
And I delete this dog
And I dount see this dog
Then Log off 