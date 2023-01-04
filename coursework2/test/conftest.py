import decimal
import pytest
from coursework2.test.shopping_basket import Basket
from coursework2.test.shopping_basket import Item


@pytest.fixture(scope='session')
def basket():
    """
    Creates a basket dictionary as a fixture
    Uses function Basket() imported from the file to be tested:
    shopping_basket.py
    """
    basket = Basket()
    return basket


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
