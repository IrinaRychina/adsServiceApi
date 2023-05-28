# Установка базового образа
FROM python:3.9

# Установка переменной окружения для Python
ENV PYTHONUNBUFFERED 1

# Создание и переключение в рабочую директорию /app
WORKDIR /adsService

# Копирование файла зависимостей в рабочую директорию контейнера
COPY requirements.txt /adsService/

# Установка зависимостей проекта
RUN pip install -r requirements.txt

# Копирование всех файлов проекта в рабочую директорию контейнера
COPY . /adsService/

# Применение миграций
RUN python manage.py migrate
