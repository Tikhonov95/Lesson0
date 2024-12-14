import requests
import pandas as pd
import numpy as np

print("=== Использование библиотеки requests ===")
response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    data = response.json()
    print("Первые 3 записи из полученного JSON:")
    for post in data[:3]:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print("Не удалось получить данные с сайта.")

print("\n=== Использование библиотеки pandas ===")
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 27, 22, 32, 29],
    "Salary": [50000, 54000, 49000, 60000, 58000]
}
df = pd.DataFrame(data)

print("Данные таблицы:")
print(df)

average_salary = df["Salary"].mean()
print("\nСредняя зарплата:", average_salary)

older_than_25 = df[df["Age"] > 25]
print("\nСотрудники старше 25 лет:")
print(older_than_25)

print("\n=== Использование библиотеки numpy ===")
array = np.array([1, 2, 3, 4, 5])

squared = array ** 2
summed = array.sum()
mean_value = array.mean()

print("Исходный массив:", array)
print("Квадраты элементов массива:", squared)
print("Сумма всех элементов:", summed)
print("Среднее значение массива:", mean_value)
