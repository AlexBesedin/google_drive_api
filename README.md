# google_drive_api

Приложение, который позволяет создавать документы в Google Drive с помощью POST-запроса.

API Документация: http://94.131.100.195/api/docs/

# Создать Google Cloud Project и настроить Google Drive API:

1. Перейти в [Google Cloud Console](https://console.cloud.google.com/)
2. Создать новый проект.
3. Включить Google Drive API для проекта.
4. Создать учетные данные для доступа к API (тип учетных данных – сервисный аккаунт).
5. Сохранить файл с учетными данными (JSON) для использования в вашем Django-приложении. Назовите файл nova.json и поместить в drive/nova.json

# Подготовка и запуск проекта

Склонируйте репозиторий:
```sh
git clone git@github.com:AlexBesedin/google_drive_api.git
```
## Создайте файл содержащий переменные виртуального окружения (.env) и добавьте секретный ключ джанго

```sh
cd google_drive_api
touch .env
```

```sh
SECRET_KEY = <Секретный ключ>
```
## Разверните контейнеры и выполните миграции:
```sh
cd google_drive_api/infra/
sudo docker-compose up -d --build
sudo docker-compose exec backend python manage.py migrate
```

## Запросы:
Чтобы создать новый документ в Google Drive с помощью нашего API, отправьте POST запрос на следующий URL:

```sh
POST http://94.131.100.195/create-document/

```
Тело запроса:
```sh
{
    "data": "Текстовое содержимое вашего документа",
    "name": "Название вашего документа",
}

```
## Ответ:
Успешный ответ будет включать сообщение о создании документа и его идентификатор в Google Drive:
```sh
{
    "message": "Документ успешно создан.",
    "link": "https://docs.google.com/document/d/1RKfMICOhf70s4SiTXP7hKnAqVjX0v7DTqIuFkZpYfJ4"
}
```

АВТОР: 

[Беседин Алексей](https://github.com/AlexBesedin)

TG: @beszedin
