import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

data = pd.read_csv('house price.csv', parse_dates=['date'])

print(data)

print(data[data['city'] == 'Medina'])


grouped_data = data.groupby(['yr_built', 'condition']).size().unstack()

fig, ax = plt.subplots(figsize=(12, 8))

for condition in grouped_data.columns:
    ax.plot(grouped_data.index, grouped_data[condition], marker='o', label=f'Condition {condition}')

plt.title('Временной ряд количества домов по годам постройки для каждого condition')
plt.xlabel('Год постройки')
plt.ylabel('Количество домов')
plt.legend(title='Condition', bbox_to_anchor=(0, 1), loc='upper left')
plt.grid(True)
plt.show()

#2

grouped_data = data.groupby(['yr_built', 'condition'])['price'].mean().unstack()

fig, ax = plt.subplots(figsize=(12, 8))

for condition in grouped_data.columns:
    ax.plot(grouped_data.index, grouped_data[condition], marker='o', label=f'Condition {condition}')

plt.title('Временной ряд средней цены по годам постройки для каждого condition')
plt.xlabel('Год постройки')
plt.ylabel('Средняя цена')
plt.legend(title='Condition', bbox_to_anchor=(0, 1), loc='upper left')
plt.grid(True)
plt.show()
#3
periods = [(1900, 1920), (1920, 1940), (1940, 1960), (1960, 1980), (1980, 2000), (2000, 2014)]

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10), sharey=True)

for period, ax in zip(periods, axes.flatten()):
    start_year, end_year = period
    data_filtered = data[(data['yr_built'] >= start_year) & (data['yr_built'] < end_year)]

    average_price_by_condition = data_filtered.groupby('condition')['price'].mean().reset_index()

    sns.barplot(x='condition', y='price', data=average_price_by_condition, ax=ax, palette="viridis")
    ax.set_title(f'Средняя цена по condition ({start_year}-{end_year})')
    ax.set_xlabel('Condition')
    ax.set_ylabel('Средняя цена')

plt.tight_layout()
plt.show()
#4
periods = [(1900, 1920), (1900, 1940), (1900, 1960), (1900, 1980), (1900, 2000), (1900, 2014)]


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10), sharey=True)


for period, ax in zip(periods, axes.flatten()):
    start_year, end_year = period
    data_filtered = data[(data['yr_built'] >= start_year) & (data['yr_built'] <= end_year)]

    average_price_by_condition = data_filtered.groupby('condition')['price'].mean().reset_index()

    sns.barplot(x='condition', y='price', data=average_price_by_condition, ax=ax, palette="viridis")
    ax.set_title(f'Средняя цена по condition ({start_year}-{end_year})')
    ax.set_xlabel('Condition')
    ax.set_ylabel('Средняя цена')

plt.tight_layout()
plt.show()

#5
periods = [(1900, 1920), (1920, 1940), (1940, 1960), (1960, 1980), (1980, 2000), (2000, 2014)]


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10), sharey=True)

for period, ax in zip(periods, axes.flatten()):
    start_year, end_year = period
    data_filtered = data[(data['yr_built'] >= start_year) & (data['yr_built'] < end_year)]

    count_by_condition = data_filtered.groupby('condition').size().reset_index(name='count')

    sns.barplot(x='condition', y='count', data=count_by_condition, ax=ax, palette="viridis")
    ax.set_title(f'Количество домов по condition ({start_year}-{end_year})')
    ax.set_xlabel('Condition')
    ax.set_ylabel('Количество домов')


plt.tight_layout()
plt.show()


#6
periods = [(1900, 1920), (1900, 1940), (1900, 1960), (1900, 1980), (1900, 2000), (1900, 2014)]


fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10), sharey=True)

for period, ax in zip(periods, axes.flatten()):
    start_year, end_year = period
    data_filtered = data[(data['yr_built'] >= start_year) & (data['yr_built'] <= end_year)]

    count_by_condition = data_filtered.groupby('condition').size().reset_index(name='count')

    sns.barplot(x='condition', y='count', data=count_by_condition, ax=ax, palette="viridis")
    ax.set_title(f'Количество домов по condition ({start_year}-{end_year})')
    ax.set_xlabel('Condition')
    ax.set_ylabel('Количество домов')


plt.tight_layout()
plt.show()
#7

grouped_data = data.groupby(['city', 'condition']).size().unstack()


fig, ax = plt.subplots(figsize=(14, 8))
sns.set_palette("viridis", len(grouped_data.columns))
grouped_data.plot(kind='barh', stacked=True, ax=ax)
plt.title('Популярность condition в каждом городе')
plt.xlabel('Количество домов')
plt.ylabel('Город')
plt.legend(title='Condition', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


average_price_by_city = data.groupby('city')['price'].mean().sort_values(ascending=False).reset_index()


plt.figure(figsize=(18, 12))
sns.barplot(x='city', y='price', data=average_price_by_city, palette='viridis')
plt.title('Средняя цена по городам')
plt.xlabel('Город')
plt.ylabel('Средняя цена')
plt.xticks(rotation=50)
plt.show()



plt.figure(figsize=(15, 8))
sns.boxplot(x='sqft_living', y='city', data=data, palette='viridis')
plt.title('Сравнение размеров жилых площадей между городами')
plt.xlabel('Жилая площадь')
plt.ylabel('Город')
plt.show()


waterfront_data = data[data['waterfront'] == 1]


grouped_data = waterfront_data.groupby('city').size().reset_index(name='Number of Homes with Waterfront')


plt.figure(figsize=(14, 8))
sns.barplot(x='city', y='Number of Homes with Waterfront', data=grouped_data, palette='viridis')
plt.title('Количество домов с доступом к воде по городам')
plt.xlabel('Города')
plt.ylabel('Количество домов с доступом к воде')
plt.xticks(rotation=45, ha='right')
plt.show()



average_price_by_waterfront = data.groupby('waterfront')['price'].mean().reset_index()

print(average_price_by_waterfront)


plt.figure(figsize=(8, 6))
sns.barplot(x='waterfront', y='price', data=average_price_by_waterfront, palette="viridis")
plt.title('Средняя цена в зависимости от близости к воде')
plt.xlabel('Близость к воде')
plt.ylabel('Средняя цена')
plt.show()


average_price_by_floors = data.groupby('floors')['price'].mean().reset_index()


plt.figure(figsize=(12, 8))
sns.lineplot(x='floors', y='price', data=average_price_by_floors, marker='o', color='b')
plt.title('Зависимость цены от количества этажей (среднее значение)')
plt.xlabel('Количество этажей')
plt.ylabel('Средняя цена')
plt.show()


count_by_floors = data.groupby('floors').size().reset_index(name='Number of Homes')


plt.figure(figsize=(12, 8))
sns.barplot(x='floors', y='Number of Homes', data=count_by_floors, palette='viridis')
plt.title('Количество домов в зависимости от количества этажей')
plt.xlabel('Количество этажей')
plt.ylabel('Количество домов')
plt.show()

results = {}

for condition_value in data['condition'].unique():
    condition_data = data[data['condition'] == condition_value]

    mode_values = condition_data.mode().iloc[0]

    results[condition_value] = mode_values

for condition_value, mode_values in results.items():
    print(f"\nCondition {condition_value} Mode Values:")
    print(mode_values)

print("Тип 1")

con_1 = data[data['condition'] == 1]
print(con_1['floors'].unique())

print("Тип 2")

con_2 = data[data['condition'] == 2]
print(con_2['floors'].unique())

print("Тип 3")

con_3 = data[data['condition'] == 3]
print(con_3['floors'].unique())

print("Тип 4")

con_4 = data[data['condition'] == 4]
print(con_4['floors'].unique())

print("Тип 5")

con_5 = data[data['condition'] == 5]
print(con_5['floors'].unique())

house_type_statistics = {}

for condition_value in data['condition'].unique():
    condition_data = data[data['condition'] == condition_value]

    stats = condition_data.describe(include='all').transpose()

    house_type_statistics[condition_value] = stats

for condition_value, stats in house_type_statistics.items():
    print(f"\nStatistics for Condition {condition_value} Houses:")
    print(stats)