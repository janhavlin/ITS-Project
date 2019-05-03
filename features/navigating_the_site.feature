Feature: Navigating the site

    Scenario: Viewing a category of products
        Given a web browser is at the E-Shop homepage
        When the user clicks on a product category that has one or more products in it
        Then products related to the category chosen are shown

    Scenario: Viewing a product
        Given a web browser is at a product category page with one or more products in it
        When the user clicks on a product image
        Then the product page is shown

    Scenario: Adding a product to Wish List
        Given a web browser is at a product page
        When user presses "Add to Wish List" button
        Then the product appears in the Wish List

    Scenario: Adding a product to Comparison
        Given a web browser is at a product page
        When the user presses the "Compare this Product" button
        Then the product is added to Product Comparison

