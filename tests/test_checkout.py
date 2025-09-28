import pytest

from app.checkout import Checkout
from app.repository.product_repository import ProductRepository



class TestCheckout:

    @pytest.fixture
    def checkout(self):
        repo = ProductRepository()
        return Checkout(repo)

    def test_no_discount(self, checkout):
        checkout.scan("MUG")
        checkout.scan("MUG")
        total = checkout.total()
        assert total == 15.0  

    def test_two_for_one_voucher(self, checkout):
        checkout.scan("VOUCHER")
        checkout.scan("VOUCHER")
        total = checkout.total()
        assert total == 5.0 

    def test_bulk_tshirt_discount(self, checkout):
        for _ in range(3):
            checkout.scan("TSHIRT")
        total = checkout.total()
        assert total == 57.0 

    def test_swag_discount(self, checkout):
        checkout.scan("VOUCHER")
        checkout.scan("TSHIRT")
        checkout.scan("MUG")
        total = checkout.total()
        assert total == 25.0

    def test_mixed_cart(self, checkout):
        checkout.scan("VOUCHER")
        checkout.scan("VOUCHER")
        checkout.scan("TSHIRT")
        checkout.scan("TSHIRT")
        checkout.scan("TSHIRT")
        checkout.scan("MUG")
        total = checkout.total()
        assert total == 70.0
