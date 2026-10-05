# E-commerce Purchase Funnel Analysis

Cool T-Shirts Inc. wants to know where shoppers abandon the purchase journey. Visit, cart, checkout and purchase logs are **left-joined** to build a per-user funnel, measure the drop-off at each stage and find the average time from first visit to purchase.

**Finding:** the *visit → add-to-cart* step loses the most users, so that is where UX work should focus.

```bash
python analysis.py   # expects data/visits.csv, cart.csv, checkout.csv, purchase.csv
```
