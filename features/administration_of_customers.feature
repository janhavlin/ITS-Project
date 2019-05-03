Feature: Administration of customers

    Scenario: Reaching the option to create a new customer
        Given the administrator is at the "Customer" Web Page
        When the administrator clicks on the "Add New Customer" button
        Then the page prompting the administrator to enter customer details appears
    
    Scenario: Adding a new user
        Given the administrator is at the "Add New Customer" Web Page
        When the administrator enters the neccessary details about the new customer
        And the administrator clicks on the "Save" button
        Then the new customer is added
    
    Scenario: Reaching the option to edit detail of a customer
        Given the administrator is at the "Customer" Web Page with one or more customers set
        When the administrator clicks on an "Edit Customer" button
        Then the page with the customer details appears
