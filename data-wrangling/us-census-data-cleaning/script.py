import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

"""temp = pd.read_csv("states0.csv")
print(temp)"""

#1
files = glob.glob("states*.csv")
df_list = list()

for file in files:
  data = pd.read_csv(file)
  df_list.append(data)

us_census = pd.concat(df_list)
print(us_census)
#print(us_census.dtypes)

#2
us_census.Income = pd.to_numeric(
  us_census.Income.replace(
    '[\$,]',
    '',
    regex = True
    ))
#print(us_census.Income)

#3
split = us_census.GenderPop.str.split("_")
#print(split)
us_census['Men'] = split.str.get(0)
us_census['Women'] = split.str.get(1)
#print(us_census.head())

#4
us_census.Men = pd.to_numeric(
  us_census.Men.replace(
    '[M\,]',
    '',
    regex = True
  ))
#print(us_census.Men)

us_census.Women = pd.to_numeric(
  us_census.Women.replace(
    '[F\,]',
    '',
    regex = True
  ))
print(us_census.Women)


#5
#print(us_census[['State', 'Women']])
us_census = us_census.fillna(
  value = {
    'Women': us_census.TotalPop - us_census.Men
  }
)
#print(us_census[['State', 'Women']])

duplicates = us_census.duplicated(subset = ['State'])
print(duplicates.value_counts())
us_census = us_census.drop_duplicates()

#6
"""
plt.scatter(us_census['Women'], us_census['Income'], color=['red','green'])
plt.xlabel('Women')
plt.ylabel('Income')
plt.show()
plt.cla() 

"""
#7
us_census['Hispanic'] = pd.to_numeric(
  us_census.Hispanic.str[:-1]
)
#print(us_census.Hispanic)
us_census['White'] = pd.to_numeric(
  us_census.White.str[:-1]
)
us_census['Black'] = pd.to_numeric(
  us_census.Black.str[:-1]
)
us_census['Native'] = pd.to_numeric(
  us_census.Native.str[:-1]
)
us_census['Asian'] = pd.to_numeric(
  us_census.Asian.str[:-1]
)
us_census['Pacific'] = pd.to_numeric(
  us_census.Pacific.str[:-1]
)
#print(us_census)

us_census = us_census.fillna(
  value ={
    'Hispanic': us_census.Hispanic.mean(),
    'White': us_census.White.mean(),
    'Black': us_census.Black.mean(),
    'Native': us_census.Native.mean(),
    'Asian': us_census.Asian.mean(),
    'Pacific': us_census.Pacific.mean()
  }
)
#print(us_census)

plt.hist(us_census['Hispanic'])
plt.title('Hispanic')
plt.show()
plt.cla()

plt.hist(us_census['White'])
plt.title('White')
plt.show()
plt.cla()

plt.hist(us_census['Black'])
plt.title('Black')
plt.show()
plt.cla()

plt.hist(us_census['Native'])
plt.title('Native')
plt.show()
plt.cla()

plt.hist(us_census['Pacific'])
plt.title('Pacific')
plt.show()
plt.cla()

plt.hist(us_census['Asian'])
plt.title('Asian')
plt.show()