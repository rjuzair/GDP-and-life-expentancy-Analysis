"""Cool T-Shirts Inc. - e-commerce purchase funnel analysis.

Joins visit, cart, checkout and purchase logs to measure drop-off at each
funnel stage and the average time from first visit to purchase.

Data: data/visits.csv, data/cart.csv, data/checkout.csv, data/purchase.csv
"""
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"


def load(name):
    return pd.read_csv(DATA_DIR / f"{name}.csv", parse_dates=[1])


def main():
    visits, cart, checkout, purchase = (load(n) for n in ("visits", "cart", "checkout", "purchase"))

    funnel = (visits.merge(cart, how="left")
                    .merge(checkout, how="left")
                    .merge(purchase, how="left"))

    visited = funnel.user_id.nunique()
    carted = funnel.loc[funnel.cart_time.notnull(), "user_id"].nunique()
    checked_out = funnel.loc[funnel.checkout_time.notnull(), "user_id"].nunique()
    purchased = funnel.loc[funnel.purchase_time.notnull(), "user_id"].nunique()

    stages = [("Visit -> Cart", visited, carted),
              ("Cart -> Checkout", carted, checked_out),
              ("Checkout -> Purchase", checked_out, purchased)]
    print("Funnel drop-off:")
    for name, before, after in stages:
        print(f"  {name:<22} {1 - after / before:6.1%} of users drop off ({before} -> {after})")

    weakest = max(stages, key=lambda s: 1 - s[2] / s[1])[0]
    print(f"\nWeakest step: {weakest}")

    funnel["time_to_purchase"] = funnel.purchase_time - funnel.visit_time
    print(f"Average time from visit to purchase: {funnel.time_to_purchase.mean()}")


if __name__ == "__main__":
    main()
