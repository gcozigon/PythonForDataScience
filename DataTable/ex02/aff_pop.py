import matplotlib.pyplot as plt
from load_csv import load

def main():
    loads = load("life_expectancy_years.csv")
    france_d = loads[loads['country'] == 'France']
    print(france_d)
    years = france_d.columns[1:]
    life_expectancy = france_d.values[0][1:]

    plt.plot(years, life_expectancy, label='France')
    plt.title('Life Expectancy in France Over the Years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()