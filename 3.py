import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv("worldcities.csv")

print(df.head())

country_counts = df['country'].value_counts()

plt.figure(figsize=(60, 40))  
country_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title("Количество записей для каждой страны", fontsize=16)
plt.xlabel("Страны", fontsize=12)
plt.ylabel("Количество записей", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

countries = df['country'].unique()

colors = plt.cm.tab20(np.linspace(0, 1, len(countries)))

plt.figure(figsize=(15, 10))

for country, color in zip(countries, colors):
    country_data = df[df['country'] == country]
    plt.scatter(
        country_data['lng'], country_data['lat'], 
        c=[color], label=country, alpha=0.6, edgecolors='black'
    )

plt.title("Карта городов (1 страна - 1 цвет)", fontsize=16)
plt.xlabel("Долгота", fontsize=12)
plt.ylabel("Широта", fontsize=12)
plt.legend(title="Страны", fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()