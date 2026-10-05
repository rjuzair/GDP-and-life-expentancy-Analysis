"""Automobile evaluation - summarising categorical data.

Frequencies, proportions and ordinal medians for a car evaluation dataset.

Data: data/car_eval_dataset.csv
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data" / "car_eval_dataset.csv"
BUYING_COST_LEVELS = ["low", "med", "high", "vhigh"]


def main():
    car_eval = pd.read_csv(DATA)
    print(car_eval.head(), "\n")

    countries = car_eval.manufacturer_country.value_counts()
    print("Cars by manufacturer country:")
    print(countries, "\n")
    print(f"Fourth most common manufacturer country: {countries.index[3]}\n")

    print("Share of cars by manufacturer country (%):")
    print((car_eval.manufacturer_country.value_counts(normalize=True) * 100).round(1), "\n")

    # buying_cost is ordinal, so the median is meaningful once categories are ordered
    buying_cost = pd.Categorical(car_eval.buying_cost, BUYING_COST_LEVELS, ordered=True)
    median_code = int(np.median(buying_cost.codes))
    print(f"Median buying cost: {BUYING_COST_LEVELS[median_code]}\n")

    print("Luggage capacity proportions (including missing):")
    print(car_eval.luggage.value_counts(dropna=False, normalize=True).round(3))


if __name__ == "__main__":
    main()
