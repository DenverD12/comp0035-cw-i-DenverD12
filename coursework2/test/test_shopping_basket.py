import decimal
import pytest
from decimal import Decimal
from test.shopping_basket import Basket
from test.shopping_basket import Item


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
    # Add item to basket as a key and value to basket dictionary
    basket.items[example_item_toastie] = "2"
    # Reset basket
    basket.reset()
    # Assert the basket dictionary should now be empty
    assert basket.items == {}

@pytest.mark.parametrize(
    "example_item_name, quantity",
    [
     ("example_item_toastie", 1),  # Try adding 1 item, quantity of 1
     ("example_item_toastie", 2),  # Try adding same item, but quantity of 2
     ("example_item_butter", 1)  # Try adding different item, quantity of 1
    ])
    # Uses the fixtures (created in conftest) passed as a string as parameters
    # Uses the item quantity a parameter
def test_when_add_item_then_basket_contains_item(
        basket, example_item_name, quantity, request):
    """
    Tests if the add_item() function adds the item successfully to
    the basket by checking if is a key in the basket dictionary.

    Args:
        basket: fixture of the shopping Basket dictionary
        example_item_name: parameter containing fixtures of 2 example items
        quantity: parameter containing quantity of each example item
        request: built in pytest fixture to obtain the value of the fixtures


    Given: An item/items (created as a fixtures in conftest.py)
    When: The item/s are added to the basket using add.item()
    Then: The item/s should be in the basket (dictionary)

    """
    # Reset basket for each test iteration
    basket.reset()
    # Obtain value of each of the fixtures such as brand_name, price
    example_item_name = request.getfixturevalue(example_item_name)

    # Add item to basket for each parameterized case
    basket.add_item(example_item_name, quantity)

    # Assert if the item for each case is in the basket dictionary
    assert example_item_name in basket.items


@pytest.mark.parametrize(
    "example_item_name, quantity, expected_result",
    [
     ("example_item_toastie", 1, 1),  # Try adding 1 item, quantity of 1
     ("example_item_toastie", 2, 2),  # Try adding same item, but quantity of 2
     ("example_item_butter", 1, 1)  # Try adding different item, quantity of 1
    ])
    # Uses the fixtures (created in conftest) passed as a string as parameters
    # Also uses specified item quantity and expected result as parameters
def test_when_add_item_then_quantity_increases(
            basket, example_item_name, quantity, expected_result, request):
    """
    Tests if the add_item() function adds the item successfully to the basket
    in terms of the quantity of item by checking if the quantity (value) of
    the key in the basket dictionary is correct

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
    # Reset basket for each test case and obtain value of fixture
    basket.reset()
    example_item_name = request.getfixturevalue(example_item_name)
    # Add item to basket for each parameterized case
    basket.add_item(example_item_name, quantity)
    # Assert if key value for added item/s is the correct expected quantity
    assert basket.items[example_item_name] == expected_result


@pytest.mark.parametrize(
    "example_item_name, quantity, expected_result",
    [
     ("example_item_toastie", -1,
      "Invalid operation - Quantity must be a positive number!"),
     ("example_item_toastie", 0,
      "Invalid operation - Quantity must be a positive number!"),
    ])
    # First test case if quantity < 0, second if quantity = 0
    # Uses a fixture (created in conftest) passed as a string as a parameter
    # Also uses a specified item quantity and expected result as parameters
    # Expected result is an error message that should be thrown if ValueError
def test_add_item_basket_error(
            basket, example_item_name, quantity, expected_result, request):
    """
    Tests if the ValueError expected custom message is thrown when an added
    item quantity is not greater than 0 is added using the add_item() function

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
    # Reset basket for each test case and obtain value of fixture
    basket.reset()
    example_item_name = request.getfixturevalue(example_item_name)
    # Add item to basket for each quantity case
    basket.add_item(example_item_name, quantity)
    # Check ValueError is thrown by asserting the correct custom error message
    assert expected_result


def test_get_total_cost(basket, example_item_toastie, example_item_butter):
    """
    Tests if the get_total_cost() function calculates the correct total
    cost of items in the basket

    Args:
        basket: fixture of the shopping Basket dictionary
        example_item_toastie: fixture of an example item created in conftest.py
        example_item_butter: fixture of different item created in contest.py

    Given: Two items (created as fixtures in conftest.py) are added to basket
    When: When the the get_total_cost() function is called
    Then: The result (total cost of items in basket) should equal the
            calculated correct expected cost
    """

    # For an empty basket case, total cost should be 0
    basket.reset()
    assert basket.get_total_cost() == 0

    # For case of adding 2 lots of two different items to basket
    basket.add_item(example_item_toastie, quantity=2)
    basket.add_item(example_item_butter, quantity=2)
    # Defining variables for price and quantity of each item in the fixtures
    price_item_toastie = decimal.Decimal('1.52')
    quantity_item_toastie = 2
    price_item_butter = decimal.Decimal('0.89')
    quantity_item_butter = 2
    # Calculation for correct expected total cost of items in basket
    expected_total_cost = (price_item_toastie*quantity_item_toastie
                           + price_item_butter*quantity_item_butter)

    # Asserting if function cost result matches the calculated total
    assert basket.get_total_cost() == expected_total_cost

