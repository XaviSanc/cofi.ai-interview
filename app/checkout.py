from typing import Counter
from app.models.discounts import DISCOUNT_PRIORITIES, Discount
from app.repository.product_repository import ProductRepository
from loguru import logger

class CheckoutException(Exception):
    pass

class Checkout:
    def __init__(self, product_repo: ProductRepository, discounts: list[Discount] = DISCOUNT_PRIORITIES):
        self.product_repo = product_repo
        self.discounts = discounts
        self.items = [] 

    def scan(self, code: str):
        
        try:
            product = self.product_repo.get_product(code)
        except ValueError as e:
            raise CheckoutException(str(e))
        
        self.items.append(product)

    def total(self)-> float:

        counts = Counter([item.code for item in self.items])
        total = 0.0

        for discount in self.discounts:
            total += discount.apply(counts)

        for code, remaining_qty in counts.items():
            if remaining_qty > 0:
                product = self.product_repo.get_product(code)
                total += remaining_qty * product.price
        return round(total, 2)