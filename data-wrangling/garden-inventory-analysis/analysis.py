import codecademylib
import pandas as pd

#1 & 2
inventory = pd.read_csv("inventory.csv")
print(inventory.head(10))

#3
staten_island = inventory.iloc[:10]
print(staten_island)

#4
product_request = staten_island.product_description
print(product_request)

#5
seed_request = inventory.loc[(inventory.location == "Brooklyn")& (inventory.product_type == "seeds")]
print(seed_request)

#6
inventory["in_stock"] = inventory.quantity.apply(lambda row: True if row > 0 else False)
print(inventory)

#7
inventory["total_value"] = inventory.price * inventory.quantity
print(inventory)

#8
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda,
axis = 1
)
print(inventory)
