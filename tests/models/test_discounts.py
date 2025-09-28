from collections import Counter
from app.models.discounts import DISCOUNT_PRIORITIES, SwagDiscount, TwoForOneVoucher, BulkTshirtDiscount

def test_swag_discount():

    counts = Counter({"VOUCHER": 1, "TSHIRT": 1, "MUG": 1})
    discount = SwagDiscount()
    total = discount.apply(counts)

    assert total == 25.0
    assert counts["VOUCHER"] == 0
    assert counts["TSHIRT"] == 0
    assert counts["MUG"] == 0

def test_two_for_one_voucher():

    counts = Counter({"VOUCHER": 3})
    discount = TwoForOneVoucher()
    total = discount.apply(counts)

    assert total == 10.0
    assert counts["VOUCHER"] == 0

def test_bulk_tshirt_discount():

    counts = Counter({"TSHIRT": 4})
    discount = BulkTshirtDiscount()
    total = discount.apply(counts)

    assert total == 76.0
    assert counts["TSHIRT"] == 0

def test_discounts_combined():

    counts = Counter({"TSHIRT": 3, "VOUCHER": 2, "MUG": 1})
    total = 0.0

    for rule in DISCOUNT_PRIORITIES:
        total += rule.apply(counts)

    expected_total = 25 + 5 + 40
    assert total == expected_total
