Feature: Test navigation between pages
  
  
  
  Scenario: Homepage can go to Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page


  Scenario: Homepage can go to Blog
    Given I am on the blog page
    When I click on the "Go to home" link
    Then  I am on the homepage