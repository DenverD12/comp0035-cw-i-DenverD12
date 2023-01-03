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


