from abc import ABC, abstractmethod
from collections import Counter

class Discount(ABC):
    @abstractmethod
    def apply(self, counts: Counter) -> float:
        """Apply discount to items and returns total"""
        pass

class SwagDiscount(Discount):
    def apply(self, counts: Counter) -> float:

        swag_sets = min(counts["VOUCHER"], counts["TSHIRT"], counts["MUG"])
        total = 0.0
        if swag_sets > 0:
            counts["VOUCHER"] -= swag_sets
            counts["TSHIRT"] -= swag_sets
            counts["MUG"] -= swag_sets
            total = swag_sets * 25
        return total

class TwoForOneVoucher(Discount):
    def apply(self, counts: Counter) -> float:

        voucher_count = counts["VOUCHER"]
        if voucher_count > 0:
            total = (voucher_count - voucher_count // 2) * 5
            counts["VOUCHER"] = 0
            return total
        return 0.0

class BulkTshirtDiscount(Discount):
    def apply(self, counts: Counter) -> float:
        
        tshirt_count = counts["TSHIRT"]
        if tshirt_count > 0:
            unit_price = 19 if tshirt_count >= 3 else 20
            total = tshirt_count * unit_price
            counts["TSHIRT"] = 0
            return total
        return 0.0

# Order of discounts to be applied
DISCOUNT_PRIORITIES = [
    SwagDiscount(),       
    TwoForOneVoucher(),
    BulkTshirtDiscount(),       
]