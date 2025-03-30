import xml.etree.ElementTree as ET
import json
import random
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Добавлен Seaborn для улучшенной визуализации


def generate_last_12_months():
    today = datetime.today()
    current_year = today.year
    current_month = today.month
    months = []
    for i in range(12):
        year = current_year
        month = current_month - i
        if month <= 0:
            month += 12
            year -= 1
        months.append(f"{year}-{month:02d}")
    months.reverse()
    return months


def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    shop = root.find('shop')
    offers = shop.find('offers').findall('offer')
    models = []
    for offer in offers:
        model_id = offer.get('id')
        model_name = offer.find('name').text
        models.append({'id': model_id, 'name': model_name})
    return models


def generate_sales_data(models, months):
    sales_data = []
    for model in models:
        sales = []
        for month in months:
            sales.append({'month': month, 'sales': random.randint(0, 100)})
        sales_data.append({
            'model_id': model['id'],
            'model_name': model['name'],
            'sales': sales
        })
    return sales_data


def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def visualize_sales(data):
    df_data = []
    for model in data:
        for sale in model['sales']:
            df_data.append({
                'Model': model['model_name'],
                'Month': sale['month'],
                'Sales': sale['sales']
            })
    df = pd.DataFrame(df_data)

    # Преобразуем данные в формат для столбчатой диаграммы
    df_pivot = df.pivot(index='Month', columns='Model', values='Sales')

    # Настройка визуализации
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(
        data=df,
        x='Month',
        y='Sales',
        hue='Model',
        palette='viridis',
        errorbar=None  # Убираем стандартную ошибку
    )

    # Дополнительные настройки
    plt.title('Динамика продаж по месяцам', fontsize=14)
    plt.xlabel('Месяц', fontsize=12)
    plt.ylabel('Количество продаж', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Добавляем подписи к столбцам
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=3)

    plt.show()

    # Вывод таблицы
    print("\nТаблица продаж:")
    print(df_pivot)


def main():
    xml_file = 'lr1.xml'  # Убедитесь, что файл существует
    json_file = 'sales.json'
    months = generate_last_12_months()
    models = parse_xml(xml_file)
    sales_data = generate_sales_data(models, months)
    save_to_json(sales_data, json_file)
    visualize_sales(sales_data)


if __name__ == "__main__":
    main()