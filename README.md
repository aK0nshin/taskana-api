# Taskana Api

## Установка
```
git clone git@github.com:aK0nshin/taskana-api.git
cd taskana-api
poetry install
cp .env.example .env
```

## Запуск API
```
uvicorn taskana_api.app:app
```

##  Миграции
```
# Сгенериировать новую миграцию
alembic revision --autogenerate -m "Title"

# Накатить миграции
alembic upgrade head
```

## Docker
```
# Сборка контейнера
docker build -t taskana-api .

# Запуск taskana-api
docker container run -p 8000:8000 taskana-api
```
