import json
from pathlib import Path

from app.models.product import Product


class ProductRepository:

    def __init__(self, config_path: str = "config/products.json"):
        self.product_catalog = {}
        self._load_products(config_path)

    def _load_products(self, config_path: str):
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Product catalog not found: {config_path}")
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data.get("products", []):
            product = Product(
                code=item["code"],
                name=item["name"],
                price=item["price"],
                currency=item.get("currency", "EUR")
            )
            self.product_catalog[product.code] = product

    def get_product(self, code: str) -> Product:
        
        if code not in self.product_catalog:
            raise ValueError(f"Product {code} not found in the catalog")
        return self.product_catalog.get(code)
        
        