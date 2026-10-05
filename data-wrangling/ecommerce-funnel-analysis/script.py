import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
"""
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())"""

#2
visits_cart = pd.merge(visits, cart, how = "left")
#print(visits_cart)

#3
print(len(visits_cart))

#4
is_null = float(len(visits_cart[visits_cart.cart_time.isnull()]))
print('There are ' + str(is_null) +' null entries')

#5
percent = (is_null/len(visits_cart)) * 100
print(str(percent) + '% people did not place order in cart')

#6 
cart_checkout = pd.merge(cart, checkout, how = 'left')
#print(cart_checkout)
null_values = float(len(cart_checkout[cart_checkout.checkout_time.isnull()]))
#print(null_values)
percent_checkout = (null_values/(len(cart_checkout)))*100
print(str(round(percent_checkout, 2)) +'% people did not proceed to checkout')

#7
all_data = visits.merge(cart, how = 'left')\
                 .merge(checkout, how ='left')\
                 .merge(purchase, how = 'left') 
                 
#print(all_data)

#8
#method 1
"""
checkout_purchase = pd.merge(checkout, purchase,how = 'left')
#print(len(checkout_purchase))
null_values1 = float(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))
#print(null_values1)
#print(len(cart_checkout) -null_values)
percent_purchase = (null_values1/(len(checkout_purchase)))*100
print(str(round(percent_purchase, 2)) +'% people did not proceed to purchase')"""

#method 2
checkout_len = float(len(all_data)) - len(all_data[all_data.checkout_time.isnull()])
#print(checkout_len)
purchase_len = len(all_data) - len(all_data[all_data.purchase_time.isnull()])
#print(purchase_len)
purchase_null = checkout_len - purchase_len
#print(purchase_null)
percent_purchase = (purchase_null)/checkout_len *100
print(str(round(percent_purchase, 2)) +'% people did not purchase')

#9
print("Visit to cart funnel section is weakest")

#10
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#11
print(all_data.time_to_purchase)

#12
print(all_data.time_to_purchase.mean())
