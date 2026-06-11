# Используем официальный Python образ
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение
COPY . .

# Открываем порт 5000 (стандартный для Flask)
EXPOSE 5000

# Команда запуска (без debug режима!)
CMD ["python", "app.py"]