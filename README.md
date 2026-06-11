# Board Games Collection

Веб-приложение для управления коллекцией настольных игр с HTTPS.

## Технологии
- Python 3.11 + Flask
- Docker & Docker Compose
- Nginx (reverse proxy)
- SQLite
- Let's Encrypt (SSL)

## Требования
- Docker
- Docker Compose
- Доменное имя (например, bbrkv.duckdns.org)
- Сервер с Ubuntu 22.04+

## Установка

### 1. Клонирование репозитория
```bash
git clone <url>
cd ProjectNastolki
```
## Получение SSL-сертификата
```
# Установка Certbot
apt install python3-pip python3-venv -y
python3 -m venv /opt/certbot/
/opt/certbot/bin/pip install certbot
ln -s /opt/certbot/bin/certbot /usr/bin/certbot

# Остановить Nginx перед получением сертификата
docker compose stop nginx

# Получить сертификат
certbot certonly --standalone -d bbrkv.duckdns.org

# Запустить Nginx обратно
docker compose start nginx
```
## Запуск приложения
```
docker compose up -d --build
```
## Проверка
Откройте в браузере: https://<your domen>

## Структура
    ProjectNastolki/
    ├── app.py                      # Основное приложение Flask
    ├── Dockerfile                  # Образ Flask
    ├── docker-compose.yml          # Оркестрация контейнеров
    ├── nginx.conf                  # Конфигурация Nginx
    ├── requirements.txt            # Зависимости Python
    ├── data.sql                    # Схема базы данных
    ├── games.db                    # SQLite база данных
    ├── templates/                  # HTML-шаблоны
    │   ├── base.html
    │   ├── index.html
    │   ├── games.html
    │   ├── add.html
    │   └── about_me.html
    └── static/                     # Статические файлы
        ├── style.css
        └── zastavka-no-bg.png
### Автор
Петров Семён
