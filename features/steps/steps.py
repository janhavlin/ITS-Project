from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',desired_capabilities = {"browserName":"chrome"})

### Feature: Administration of customers
def admin_login(context):
    
    element = driver.find_element_by_xpath('//*[@id="input-username"]')
    element.send_keys('admin')
    element = driver.find_element_by_xpath('//*[@id="input-password"]')
    element.send_keys('admin')  # security first :-)
    element = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button')
    element.click()

# Scenario: Reaching the option to create a new customer
@given('the administrator is at the "Customer" Web Page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="customer"]/a/i')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="customer"]/ul/li[1]/a')
    element.click()

@when('the administrator clicks on the "Add New Customer" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a')
    element.click()
    
@then('the page prompting the administrator to enter customer details appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-firstname"]')
    

# Scenario: Adding a new user
@given('the administrator is at the "Add New Customer" Web Page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="customer"]/a/i')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="customer"]/ul/li[1]/a')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a')
    element.click()

@when('the administrator enters the neccessary details about the new customer')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-firstname"]')
    element.send_keys('Jan')
    element = driver.find_element_by_xpath('//*[@id="input-lastname"]')
    element.send_keys('Novak')
    element = driver.find_element_by_xpath('//*[@id="input-email"]')
    element.send_keys('jn@seznam.cz')
    element = driver.find_element_by_xpath('//*[@id="input-telephone"]')
    element.send_keys('111222333')
    element = driver.find_element_by_xpath('//*[@id="input-password"]')
    element.send_keys('1234')
    element = driver.find_element_by_xpath('//*[@id="input-confirm"]')
    element.send_keys('1234')
    
@when('the administrator clicks on the "Save" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button')
    element.click()

@then('the new customer is added')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]')

# Scenario: Reaching the option to edit detail of a customer
@given('the administrator is at the "Customer" Web Page with one or more customers set')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="customer"]/a/i')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="customer"]/ul/li[1]/a')
    element.click()

@when('the administrator clicks on an "Edit Customer" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="form-customer"]/div/table/tbody/tr/td[8]/a')
    element.click()

@then('the page with the customer details appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button')

### Feature: Administration of orders
# Scenario: Reaching the option to create a new order
@given('the administrator is at the "Orders" Web Page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="sale"]')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="sale"]/ul/li[1]/a')
    element.click()

@when('the administrator clicks on the "Add New Order" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a')
    element.click()

@then('the page prompting the administrator to enter order details appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-firstname"]')

# Scenario: Reaching the option to edit detail of an order
@given('the administrator is at the "Orders" Web Page with one or more orders set')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="sale"]')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="sale"]/ul/li[1]/a')
    element.click()

@when('the administrator clicks on an "Edit Order" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="form-order"]/div/table/tbody/tr/td[8]/a[2]')
    element.click()

@then('the page with the order details appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-firstname"]')


### Feature: Administration of products
# Scenario: Reaching the option to add a new product
@given('the administrator is at the "Product List" Web Page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="catalog"]/a')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a')
    element.click()

@when('the administrator clicks on the "Add New Product" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a')
    element.click()

@then('the page prompting the administrator to enter product details appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-name1"]')

# Scenario: Adding a new product
@given('the administrator is at the "Add product" Web Page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="catalog"]/a')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a')
    element.click()

@when('the administrator enters the neccessary details about the new product')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-name1"]')
    element.send_keys("Product name")
    element = driver.find_element_by_xpath('//*[@id="input-meta-title1"]')
    element.send_keys("Title")

    element = driver.find_element_by_xpath('//*[@id="form-product"]/ul/li[2]/a')
    element.click()
    
    element = driver.find_element_by_xpath('//*[@id="input-model"]')
    element.send_keys("Model")

#@when('the administrator clicks on the "Save" button')
#def step_impl(context):
#    element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button')
#    element.click()

@then('the new product is added')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]')

# Scenario: Reaching the option to edit details of a product
@given('the administrator is at the "Product List" Web Page with one or more products set')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/admin/')
    admin_login(context)
    element = driver.find_element_by_xpath('//*[@id="catalog"]/a')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="catalog"]/ul/li[2]/a')
    element.click()

@when('the administrator clicks on an "Edit Product" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr[1]/td[8]/a')
    element.click()

@then('the page with the product details appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-name1"]')

### Feature: Buying process
# Scenario: Adding a product to Cart    
#@given('a web browser is at a product page')
@when('the user enters quantity of the product')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="input-quantity"]')
    element.send_keys('1')

@when('the user presses "Add to Cart" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="button-cart"]')
    element.click()

@then('the product appears in the Cart')
def step_impl(context):
    element = driver.find_element_by_xpath('/html/body/div[2]/div[1]')

# Scenario: Viewing the Shopping Cart
@given('a web browser is at any E-Shop page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/index.php?route=common/home')

@when('the user presses "Shopping Cart" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="cart"]/button')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="cart"]/ul/li[2]/div/p/a[1]')
    element.click()

@then('the Shopping Cart page appears')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/a')
    
# Scenario: Checking out
@given('a web browser is at the Cart page with one or more products in the Cart')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/index.php?route=checkout/cart')

@when('the user presses the "Checkout" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[2]/a')
    element.click()

@then('the user is prompted to enter checkout options')
def step_impl(context):
    element = driver.find_element_by_xpath('/html/body/div[2]/ul/li[3]/a')

### Feature: Navigating the site
# Scenario: Viewing a category of products
@given('a web browser is at the E-Shop homepage')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/index.php?route=common/home')

@when('the user clicks on a product category that has one or more products in it')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/a')
    element.click()
    element = driver.find_element_by_xpath('//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a')
    element.click() 
    
@then('products related to the category chosen are shown')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/h2')

# Scenario: Viewing a product
@given('a web browser is at a product category page with one or more products in it')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/index.php?route=product/category&path=20_27')
    
@when('the user clicks on a product image')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div[2]/div[1]/h4/a')
    element.click()
    

@then('the product page is shown')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="button-cart"]')
    #assert context.failed is False

# Scenario: Adding a product to Wish List
@given('a web browser is at a product page')
def step_impl(context):
    driver.get('http://mys01.fit.vutbr.cz:8017/index.php?route=product/product&product_id=43')
    
@when('user presses "Add to Wish List" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/button[1]')
    element.click()

@then('the product appears in the Wish List')
def step_impl(context):
    element = driver.find_element_by_xpath('/html/body/div[2]/div[1]')

# Scenario: Viewing the Wish List
# Scenario: Adding a product to Comparison
#@given('a web browser is at a product page')       # Already defined

@when('the user presses the "Compare this Product" button')
def step_impl(context):
    element = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/button[2]')
    element.click()
    
@then('the product is added to Product Comparison')
def step_impl(context):
    element = driver.find_element_by_xpath('/html/body/div[2]/div[1]')

# Scenario: Viewing the Product Comparison page
