Feature: Buying process

    Scenario: Adding a product to Cart
        Given a web browser is at a product page
        When the user enters quantity of the product
        And the user presses "Add to Cart" button
        Then the product appears in the Cart
    
    Scenario: Viewing the Shopping Cart
        Given a web browser is at any E-Shop page
        When the user presses "Shopping Cart" button
        Then the Shopping Cart page appears

    Scenario: Checking out
        Given a web browser is at the Cart page with one or more products in the Cart
        When the user presses the "Checkout" button
        Then the user is prompted to enter checkout options
