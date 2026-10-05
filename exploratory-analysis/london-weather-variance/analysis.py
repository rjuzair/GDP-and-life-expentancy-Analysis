"""London weather - variance and standard deviation of temperature.

How much does London's temperature vary over the year and within each month?

Data: data/london_weather.csv with at least `month` and `TemperatureC`
columns (hourly readings).
"""
from pathlib import Path

import calendar

import pandas as pd

DATA = Path(__file__).parent / "data" / "london_weather.csv"


def main():
    london_data = pd.read_csv(DATA)
    temperature = london_data.TemperatureC
    print(f"Readings: {len(london_data)}")
    print(f"Annual mean: {temperature.mean():.2f} °C, "
          f"variance: {temperature.var(ddof=0):.2f}, std: {temperature.std(ddof=0):.2f}\n")

    monthly = (london_data.groupby("month").TemperatureC
               .agg(mean="mean", std=lambda s: s.std(ddof=0))
               .round(2))
    monthly.index = [calendar.month_name[m] for m in monthly.index]
    print("Monthly temperature (°C):")
    print(monthly)


if __name__ == "__main__":
    main()
