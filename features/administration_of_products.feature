Feature: Administration of products

    Scenario: Reaching the option to add a new product
        Given the administrator is at the "Product List" Web Page
        When the administrator clicks on the "Add New Product" button
        Then the page prompting the administrator to enter product details appears

    Scenario: Adding a new product
        Given the administrator is at the "Add product" Web Page
        When the administrator enters the neccessary details about the new product
        And the administrator clicks on the "Save" button
        Then the new product is added

    Scenario: Reaching the option to edit details of a product
        Given the administrator is at the "Product List" Web Page with one or more products set
        When the administrator clicks on an "Edit Product" button
        Then the page with the product details appears
