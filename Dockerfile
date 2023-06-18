#FROM ubuntu:latest
#LABEL authors="bekhan"
#
#ENTRYPOINT ["top", "-b"]

# Базовый образ
FROM python:3.9

# Установка зависимостей
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование кода приложения
COPY . /app

# Рабочая директория
WORKDIR /app

# Запуск миграций и приложения
RUN python manage.py migrate

# Открытие порта
EXPOSE 8000

# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
