

from app.checkout import Checkout
from app.repository.product_repository import ProductRepository


def main():
    repo = ProductRepository()
    checkout = Checkout(repo)

    checkout.scan("VOUCHER")
    checkout.scan("VOUCHER")
    checkout.scan("VOUCHER")
    checkout.scan("TSHIRT")
    checkout.scan("MUG")

    total_amount = checkout.total()
    print(f"Total amount: {total_amount} €")

if __name__ == "__main__":
    main()
