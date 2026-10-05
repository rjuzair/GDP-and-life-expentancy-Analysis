import pandas as pd
import numpy as np
car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

modal_category = car_eval['manufacturer_country'].value_counts()
print(modal_category)
print(modal_category.index[3])

manufacturer_percentile = (car_eval['manufacturer_country'].value_counts(normalize = True, dropna = False)) * 100
print(manufacturer_percentile)

print(car_eval['buying_cost'])

buying_cost_categories =  ['low', 'med', 'high', 'vhigh']
print(buying_cost_categories)

car_eval['buying_cost'] = pd.Categorical(
  car_eval['buying_cost'],
  ['low', 'med', 'high', 'vhigh'],
  ordered = True
)
print(car_eval['buying_cost'])

median = np.median(car_eval['buying_cost'].cat.codes)
median = buying_cost_categories[int(median)]
print(median)

luggage_por = car_eval.luggage.value_counts(dropna = False, normalize = True)
print(luggage_por)

luggage_por = car_eval.luggage.value_counts(dropna = False)/len(car_eval.luggage)
print(luggage_por)