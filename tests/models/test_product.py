
from app.models.product import Product

def test_product_creation():
    p = Product("VOUCHER", "Cofi Voucher", 5.0)
    assert p.code == "VOUCHER"
    assert p.name == "Cofi Voucher"
    assert p.price == 5.0
    assert p.currency == "EUR"  # default
