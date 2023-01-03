import decimal
import pytest
from decimal import Decimal
from test.shopping_basket import Basket
from test.shopping_basket import Item

@pytest.fixture(scope='session')
def basket():
    basket = Basket()
    return basket

@pytest.fixture(scope='session')
def example_item_toastie():
    example_item_toastie = Item(brand_name='Warburtons', product_name='Toastie', description='800g white sliced loaf', price=decimal.Decimal('1.52'))
    yield example_item_toastie

@pytest.fixture(scope='session')
def example_item_butter():
    example_item_butter = Item(brand_name='Flora', product_name='Buttery', description='Buttery spread', price=decimal.Decimal('0.89'))
    yield example_item_butter
