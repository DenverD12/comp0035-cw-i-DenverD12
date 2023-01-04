# **Unit Testing**

# **Creating fixtures in conftest.py**
## **Import required libraries**
```
import decimal
import pytest
from coursework2.test.shopping_basket import Basket
from coursework2.test.shopping_basket import Item
```
- The first import is for converting the prices to decimal floating point value.
- The second import for pytest allows for pytest fixtures to be created.
- The third import line imports the Basket class from the file shopping_basket.py (the file to be tested).
- The final import line imports the Item class from the file shopping_basket.py (the file to be tested).

<br/>

## **Creating pytest fixtures**
Firstly, fixtures were created in a new file called conftest.py. This is to prevent repeating calling functions for each test.
### **Fixture for a basket object**
```
@pytest.fixture(scope='session')
def basket():
    """
    Creates a basket dictionary as a fixture
    Uses function Basket() imported from the file to be tested:
    shopping_basket.py
    """
    basket = Basket()
    return basket
```
- This function is a pytest fixture that calls the `Basket()` class function from the `shopping_basket.py` file which is being tested, to create an instance of a basket to hold the items (also created as fixtures). 
- This will then be used in the testing file `test_shopping_basket` for each test, which is more convenient than writing out the function for each test.

<br/>
<br/>

### **Fixture for the first example item: toastie**
```
@pytest.fixture(scope='session')
def example_item_toastie():
    """
    Creates an item, as a fixture using the Item() function
    from the file to be tested: shopping_basket.py
    """
    example_item_toastie = Item(
        brand_name='Warburtons', product_name='Toastie',
        description='800g white sliced loaf', price=decimal.Decimal('1.52'))
    yield example_item_toastie

```


### **Fixure for second example item: butter**
```
@pytest.fixture(scope='session')
def example_item_butter():
    """
    Creates another item using the Item() function in the file to be tested:
    shopping_basket.py
    """
    example_item_butter = Item(
        brand_name='Flora', product_name='Buttery',
        description='Buttery spread', price=decimal.Decimal('0.89')
        )
    yield example_item_butter
```
- The above 2 functions are pytest fixtures that call the `Item()` class function from `shopping_basket.py` (the file being tested) to create two different example item objects, with arbitrary specified example parameters that can be called upon in testing.
- The price is defined with `decimal.Decimal()` to ensure the correct type of decimal floating point arithmetic is used, so it is consistent with the file being tested for arithmetic calculations.
- These fixtures will be used in the test file `test_shopping_basket.py` as example item parameters, which is more convenient than writing out the function again for each test.

<br/>
<br/>

# **Testing file test_shopping_basket.py**
## **Importing required libraries again**
```
import decimal
import pytest

```
- The decimal library was imported for the same reason as in conftest.py
- The pytest library was imported this time to utilise the mark.parametrize feature which allows for parametrization, simplifying the use of multiple test use cases.

<br/>

## **Testing reset() function in the Basket() class**
```
def test_reset(basket, example_item_toastie):
    """
    Tests if reset() function resets basket contents to give empty dictionary

    Fixtures used (created in conftest.py):
        basket: fixture of the shopping Basket dictionary
        example_item_toastie: fixture of an example item

    Given: An item (created as a fixture) is in the basket (created as fixture)
    When: The reset() function is called to reset the basket contents
    Then: There should be no items in the basket
    """

    basket.items[example_item_toastie] = "2"
    basket.reset()
    assert basket.items == {}
```
This test function was used to test the reset() function in the basket class by checking if the basket dictionary is empty after it is called.
<br/>

**Breaking down `test_reset()` function:**
```
basket.items[example_item_toastie] = "2"
```
The line of code above adds a dictionary item with a key of "example_item_toastie" and a value (quantity) of 2. This was done just to ensure the basket was not already empty (i.e. ensure that it contained something), in order to then reset its contents.
```
basket.reset()
```
The line of code above executes the reset() function from the main `shopping_basket.py` file, which is what is being tested.
```
assert basket.items == {}
```
The above line of code asserts that the dictionary of the basket after the reset is an empty dictionary. 
This indicates that if the test is successful, then the reset function, which is supposed to empty the basket, has worked.


<br/>

## **First test of the add_item() function in Basket() class, checking  if the item is in the basket dictionary**
```
@pytest.mark.parametrize("example_item_name, quantity", 
[("example_item_toastie", 1), ("example_item_toastie", 2), ("example_item_butter", 1)])
def test_when_add_item_then_basket_contains_item(basket, example_item_name, quantity, request):
    """
    Tests if the add_item() function adds the item successfully to the basket by checking if is a key in the basket dictionary.

    Args:
        basket: fixture of the shopping Basket dictionary
        example_item_name: parameter containing fixtures of 2 example items
        quantity: parameter containing quantity of each example item
        request: built in pytest fixture to obtain the value of the fixtures


    Given: An item/items (created as a fixtures in conftest.py)
    When: The item/s are added to the basket using add.item()
    Then: The item/s should be in the basket (dictionary)

    """

    basket.items.clear()
    example_item_name = request.getfixturevalue(example_item_name)
    basket.add_item(example_item_name, quantity)
    assert example_item_name in basket.items
```
This test function tests if the add_item() function works in terms of if the added item is in the basket dictionary.  
<br/>


Parametrization for 3 possible test cases:

```
@pytest.mark.parametrize("example_item_name, quantity", 
[("example_item_toastie", 1), ("example_item_toastie", 2), ("example_item_butter", 1)])
```
- This parametrization feature uses the fixtures (created in conftest.py) passed as a string, as the parameter called "example_item_name". This is the name of each example item fixture created before.
- The value of the fixture is collected later, using the built-in pytest fixture called request. 
- The parametrization uses the item quantity as "quantity" as the second parameter, which is changed for each test case.
<br/>

Each test case:
<br/>

Test case 1: Adding 1 of an item (toastie) to the basket  

`("example_item_toastie", 1)`  

<br/>

Test case 2: Adding 2 of the same item to the basket

`("example_item_toastie", 2)`  

<br/>

Test case 3: Adding 1 of a different item (butter) to the basket

`("example_item_butter", 1)` 

<br/>

**Breaking down `test_when_add_item_then_basket_contains_item()` function:**
```
basket.items.clear()
```
The above line of code clears the basket dictionary to ensure an empty basket for each iteration of the parametrized test cases. This is for accuracy in each test.
```
example_item_name = request.getfixturevalue(example_item_name)
```
The line of code above uses a built-in pytest fixture called request to obtain the value of the fixtures (example items) which were passed as string parameters.
```
    basket.add_item(example_item_name, quantity)
```
The line of code above calls the add_item() function in the Basket() class of the function to be tested `shopping_basket.py`.  
Each test case with the corresponding example item and quantity is passed through as parameters.
```
assert example_item_name in basket.items
```
This asserts that the example item for each test case is in the basket dictionary to test if the add_item() function works in terms of if the item is contained in the basket.
<br/>

## **Second test of the add_item() function in Basket() class, checking for correct quantity**
```
@pytest.mark.parametrize("example_item_name, quantity, expected_result",
    [("example_item_toastie", 1, 1),  
     ("example_item_toastie", 2, 2),  
     ("example_item_butter", 1, 1)])
def test_when_add_item_then_quantity_increases(basket, example_item_name, quantity, expected_result, request):
    """
    Tests if the add_item() function adds the item successfully to the basket in terms of the quantity of item by checking if the quantity (value) of the key in the basket dictionary is correct

    Args:
        basket: fixture of the shopping Basket dictionary
        example_item_name: parameter containing fixtures of 2 example items
        quantity: parameter containing quantity of each example item
        expected_result: parameter containing expected result of the item key
        request: built in pytest fixture to obtain the value of the fixtures


    Given: An item/items (created as a fixtures in conftest.py)
    When: The item/s are added to the basket using add.item()
    Then: The item/s should be in the basket (dictionary)

    """
    basket.items.clear()
    example_item_name = request.getfixturevalue(example_item_name)
    basket.add_item(example_item_name, quantity)
    assert basket.items[example_item_name] == expected_result
```

<br/>

Parametrization for 3 possible test cases:

```
@pytest.mark.parametrize("example_item_name, quantity, expected_result",
    [("example_item_toastie", 1, 1), ("example_item_toastie", 2, 2), ("example_item_butter", 1, 1)])
```
- This parametrization feature uses the fixtures (created in conftest.py) passed as a string, as the parameter called "example_item_name". This is the name of each example item fixture created before.
- The value of the fixture is collected later, using the built-in pytest fixture called request. 
- The parametrization uses the item quantity as "quantity" as the second parameter, which is changed for each test case.
- The final parameter is "expected_result" and refers to the correct expected quantity of the basket after the add_item() function is called.
<br/>

Each test case:
<br/>

Test case 1: Adding 1 of an item (toastie) to the basket  

`("example_item_toastie", 1, 1)`  

- The expected result of quantity in the basket for this case should be 1
<br/>

Test case 2: Adding 2 of the same item to the basket

`("example_item_toastie", 2, 2)`  

- The expected result of quantity in the basket for this case should be 2
<br/>

Test case 3: Adding 1 of a different item (butter) to the basket

`("example_item_butter", 1, 1)` 

- The expected result of quantity in the basket for this case should be 1  

<br/>

**Breaking down `test_when_add_item_then_quantity_increases()` function:**
```
basket.items.clear()
```
The above line of code clears the basket dictionary to ensure an empty basket for each iteration of the parametrized test cases. This is for accuracy in each test.
```
example_item_name = request.getfixturevalue(example_item_name)
```
The line of code above uses a built-in pytest fixture called request to obtain the value of the fixtures (example items) which were passed as string parameters.
```
basket.add_item(example_item_name, quantity)
```
The line of code above calls the add_item() function in the Basket() class of the function to be tested `shopping_basket.py`.  
Each test case with the corresponding example item and quantity is passed through as parameters.
```
assert basket.items[example_item_name] == expected_result
```
The line of code above asserts that the value of the key with the name of each example item is the same as the defined correct expected result value for each of the 3 test cases. This tests if the quantity of the basket has been updated correctly after the add_item() function was used.

<br/>

## **Third test of the add_item() function in Basket() class, checking for errors thrown when the quantity added is not greater than 0**
```
@pytest.mark.parametrize("example_item_name, quantity, expected_result",
    [("example_item_toastie", -1, "Invalid operation - Quantity must be a positive number!"),
     ("example_item_toastie", 0, "Invalid operation - Quantity must be a positive number!"),])
def test_add_item_not_greater_than_zero(basket, example_item_name, quantity, expected_result, request):
    """
    Tests if the ValueError expected custom message is thrown when an added item quantity is not greater than 0 is added using the add_item() function

    Args:
        basket: fixture of the shopping Basket dictionary
        example_item_name: parameter containing fixtures of 2 example items
        quantity: parameter containing quantity of each example item
        expected_result: parameter containing expected error message
        request: built in pytest fixture to obtain the value of the fixtures

    Given: An item (created as a fixtures in conftest.py)
    When: The item is added to basket using add.item() with a quantity < or = 0
    Then: ValueError should be raised and caught, throwing a custom message:
    "Invalid operation - Quantity must be a positive number!"
    """

    basket.items.clear()
    example_item_name = request.getfixturevalue(example_item_name)
    basket.add_item(example_item_name, quantity)
    assert expected_result
```
<br/>

Parametrization for 2 possible test cases:
```
@pytest.mark.parametrize("example_item_name, quantity, expected_result",
    [("example_item_toastie", -1, "Invalid operation - Quantity must be a positive number!"),
     ("example_item_toastie", 0, "Invalid operation - Quantity must be a positive number!"),])
```
The parametrization feature is the same concept as the previous function, except that the quantity is now -1 and 0 and the expected_result should be a custom error message that was defined in the `shopping_bakset.py` file: "Invalid operation - Quantity must be a positive number!".  
The ValueError cannot be caught itself because it is caught by the exception block which throws an error message defined above but testing for this message confirms the error works correctly and that the ValueError had indeed been thrown but caught by the exception block.
<br/>

Each test case:
<br/>

Test case 1: For quantity < 0
`("example_item_toastie", -1, "Invalid operation - Quantity must be a positive number!")`
<br/>

Test case 2: For quantity = 0
("example_item_toastie", 0, "Invalid operation - Quantity must be a positive number!")
<br/>

**Breaking down `test_add_item_not_greater_than_zero()` function:**
```
basket.items.clear()
```
The above line of code clears the basket dictionary to ensure an empty basket for each iteration of the parametrized test cases. This is for accuracy in each test.
```
example_item_name = request.getfixturevalue(example_item_name)
```
The line of code above uses a built-in pytest fixture called request to obtain the value of the fixtures (example items) which were passed as string parameters.
```
basket.add_item(example_item_name, quantity)
```
The line of code above calls the add_item() function in the Basket() class of the function to be tested `shopping_basket.py`.  
Each test case with the corresponding example item and quantity is passed through as parameters.
```
assert expected_result
```
This code asserts the custom error message which should be thrown for each test case which tests if the ValueError is thrown, if the quantity of items added with add_item() function is not greater than 0.
<br/>

## **Testing the total_cost() function**
```
def test_get_total_cost(basket, example_item_toastie, example_item_butter):
    """
    Tests if the get_total_cost() function calculates the correct total cost of items in the basket

    Args:
        basket: fixture of the shopping Basket dictionary
        example_item_toastie: fixture of an example item created in conftest.py
        example_item_butter: fixture of different item created in contest.py

    Given: Two items (created as fixtures in conftest.py) are added to basket
    When: When the the get_total_cost() function is called
    Then: The result (total cost of items in basket) should equal the calculated correct expected cost
    """

    basket.items.clear()
    assert basket.get_total_cost() == 0

    basket.add_item(example_item_toastie, quantity=2)
    basket.add_item(example_item_butter, quantity=2)
    price_item_toastie = decimal.Decimal('1.52')
    quantity_item_toastie = 2
    price_item_butter = decimal.Decimal('0.89')
    quantity_item_butter = 2
    expected_total_cost = (price_item_toastie*quantity_item_toastie + price_item_butter*quantity_item_butter)

    assert basket.get_total_cost() == expected_total_cost
```
<br/>

**Breaking down `test_add_item_not_greater_than_zero()` function:**
```
basket.items.clear()
assert basket.get_total_cost() == 0
```
- The first line of code above resets the basket to test the case of an empty basket
- The second line asserts that the total cost found by the get_total_cost() function should be 0.
<br/>

```
basket.add_item(example_item_toastie, quantity=2)
basket.add_item(example_item_butter, quantity=2)
```
The first line of code above adds each item (created as fixtures in conftest.py) of example_item_toastie and example_item_butter, each with a quantity of 2.  
<br/>

```
price_item_toastie = decimal.Decimal('1.52')
quantity_item_toastie = 2
price_item_butter = decimal.Decimal('0.89')
quantity_item_butter = 2
```
- The lines of code above define a comparison variable for the price of each of the items in the fixures (i.e. one variable for toastie and one for butter).  
- The price for each is ensured to be identical to the corresponding item created in fixtures; `price_item_toastie` ensured to match the price of the `example_item_toastie` price argument and `price_item_butter` matches the price pf `example_item_butter` fixture in conftest.py.  
- The quantity of both items is set to be 2, to match the quantity added to each of the add_item() functions executed in the lines before.
- These must match to ensure testing accuracy.  

```
expected_total_cost = (price_item_toastie*quantity_item_toastie + price_item_butter*quantity_item_butter)
```
The line above creates a total cost calculation, which is what the total_cost() function being tested should do.  
This is assigned to a variable `expected_total_cost`.
```
assert basket.get_total_cost() == expected_total_cost
```
This asserts that the function being tested should return the correct value that matches the expected_total_cost, given the function being tested `get_total_cost()` works correctly.

## **Evidence for all tests working:"
### For terminal output of all 10 tests:
Link to evidence image: https://github.com/ucl-comp0035/comp0035-cw-i-DenverD12/blob/master/coursework2/testing_success_evidence_terminal_output.png 
<br/>

If link doesn't work locate the screenshot in file path:  
`ucl-comp0035/comp0035-cw-i-DenverD12/coursework2/testing_success_evidence_terminal_output.png`
<br/>
<br/>

### For filepaths and all test names showing success in the Testing section:
Link to evidence image: https://github.com/ucl-comp0035/comp0035-cw-i-DenverD12/blob/master/coursework2/testing_success_evidence_with_filepaths.png
<br/>

If link doesn't work locate the screenshot in file path:  
`ucl-comp0035/comp0035-cw-i-DenverD12/coursework2/testing_success_evidence_with_filepaths.png`
<br/>
<br/>

### For continuous integration containing linting and unit testing evidence:
**See `tools-techniques-2.md` file**
