"""Petal Power - garden store inventory analysis.

Uses pandas selection, boolean filtering and row-wise transformations to
answer stock questions for a chain of garden stores.

Data: data/inventory.csv (location, product_type, product_description,
quantity, price)
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data" / "inventory.csv"


def main():
    inventory = pd.read_csv(DATA)

    staten_island = inventory[inventory.location == "Staten Island"]
    print("Staten Island products:")
    print(staten_island.product_description.to_string(index=False), "\n")

    seed_request = inventory[(inventory.location == "Brooklyn") & (inventory.product_type == "seeds")]
    print("Seeds available in Brooklyn:")
    print(seed_request, "\n")

    inventory["in_stock"] = inventory.quantity > 0
    inventory["total_value"] = inventory.price * inventory.quantity
    inventory["full_description"] = inventory.product_type + " - " + inventory.product_description

    print("Inventory value by location:")
    print(inventory.groupby("location").total_value.sum().sort_values(ascending=False))
    print(f"\nOut-of-stock products: {(~inventory.in_stock).sum()}")


if __name__ == "__main__":
    main()
