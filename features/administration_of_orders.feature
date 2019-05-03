Feature: Administration of orders

    Scenario: Reaching the option to create a new order
        Given the administrator is at the "Orders" Web Page
        When the administrator clicks on the "Add New Order" button
        Then the page prompting the administrator to enter order details appears
    
    Scenario: Reaching the option to edit detail of an order
        Given the administrator is at the "Orders" Web Page with one or more orders set
        When the administrator clicks on an "Edit Order" button
        Then the page with the order details appears
