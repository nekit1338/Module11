import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""Комбинированное использование библиотек requests и pillow"""

url = 'https://www.allthingswild.co.uk/wp-content/uploads/2022/01/MAGNET-Capybara-1.jpg'


response = requests.get(url)
response.raise_for_status()

# Сохраняем изображение во временный файл
with open('img.jpg', 'wb') as file:
    for i in response.iter_content(1024):
        file.write(i)

# Открываем изображение с помощью Pillow
img = Image.open('img.jpg')

# Уменьшаем размер изображения
new_size = (img.width // 2, img.height // 2)
img = img.resize(new_size)

# Сохраняем новое изображение
img.save('resized_img.jpg')

"""Комбинированное использование библиотек numpy и matplotlib"""

"""Случайное блуждание - математическая модель, описывающая случайное движение частицы"""

# Задаем количество шагов
num_steps = 1000

# Создаем массив для хранения значений случайного блуждания
random_walk = np.random.randn(num_steps).cumsum()

# Создаем график
plt.plot(random_walk)
plt.title('Случайное блуждание')
plt.xlabel('Шаг')
plt.ylabel('Значение')
plt.grid(True)
plt.show()
