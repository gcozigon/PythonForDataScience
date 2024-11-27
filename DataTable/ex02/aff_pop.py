import pandas as pd
import matplotlib.pyplot as plt

def convert_to_million(value):
    if 'K' in value:
        return float(value.replace('K', '')) / 1000
    elif 'M' in value:
        return float(value.replace('M', ''))
    else:
        return float(value) / 1000000 

loads = pd.read_csv("population_total.csv")

france_d = loads[loads['country'] == 'France']
angola_d = loads[loads['country'] == 'Angola']

years = france_d.columns[1:]
france_population = france_d.values[0][1:]
angola_population = angola_d.values[0][1:]

france_population = [convert_to_million(value) for value in france_population]
angola_population = [convert_to_million(value) for value in angola_population]

years = [year for year in years if int(year) <= 2050]
france_population = france_population[:len(years)]
angola_population = angola_population[:len(years)]

plt.figure(figsize=(10, 6))

plt.plot(years, france_population, label="France", color='blue')
plt.plot(years, angola_population, label="Angola", color='red')

plt.title("Total Population Over Time")
plt.xlabel("Year")
plt.xticks(years[::40], rotation=45)
plt.ylabel("Total Population (Millions)")
plt.legend()


plt.show()
