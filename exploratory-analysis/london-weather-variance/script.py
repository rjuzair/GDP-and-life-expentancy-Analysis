import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#1.
print(london_data.head())


#2
print(len(london_data))

#3
temp_clmn = london_data.TemperatureC
#print(temp_clmn)

avg_temp = np.mean(temp_clmn)
print(avg_temp)


temp_var = np.var(temp_clmn)
#print(temp_var)

temp_std = np.std(temp_clmn)
print(temp_std)

#8
june = london_data.loc[
  london_data["month"] == 6]["TemperatureC"]
print(june)

july = london_data.loc[london_data.month == 7].TemperatureC
print(july)

june_mean = np.mean(june)
july_mean = np.mean(july)

print(june_mean)
print(july_mean)

print(np.std(june))
print(np.std(july))

for i in range(1, 13):

  month = london_data.loc[london_data.month == i
  ].TemperatureC
  print("The mean temperature in month " +str(i)+ " is " + str(np.mean(month)))
  print("The standard Deviation of temperature in month " +str(i)+ " is "+ str(np.std(month))+"\n")