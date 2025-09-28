import pytest

from app.models.product import Product
from app.repository.product_repository import ProductRepository

def test_get_existing_product():
    repo = ProductRepository()
    product = repo.get_product("VOUCHER")

    assert isinstance(product, Product)
    assert product.code == "VOUCHER"
    assert product.name == "Cofi Voucher"
    assert product.price == 5.0
    assert product.currency == "EUR"


def test_get_nonexistent_product_raises():
    repo = ProductRepository()

    with pytest.raises(ValueError) as exc_info:
        repo.get_product("NON_EXISTENT")

    assert "Product NON_EXISTENT not found in the catalog" in str(exc_info.value)
