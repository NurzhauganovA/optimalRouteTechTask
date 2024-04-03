# optimalRouteTechTask
Technical Task company "WelbeX"

Этот проект представляет собой простое приложение на FastAPI для работы с маршрутами. Приложение позволяет создавать маршруты, загружать данные о точках маршрута из CSV файла, находить оптимальный маршрут методом ближайшего соседа и получать информацию о маршрутах.

## Установка и запуск

1. Клонируйте репозиторий:

   ```sh
   git clone https://github.com/NurzhauganovA/optimalRouteTechTask.git

   1. Перейдите в директорию проекта:
   cd optimalRouteTechTask

   2. Запустите Docker контейнеры для приложения и базы данных:
   make all

   3. Приложение будет доступно по адресу `http://localhost:7777`.

## Использование

1. Для создания маршрута отправьте POST запрос на /api/routes с данными в формате JSON.
2. Для загрузки данных о точках маршрута из CSV файла отправьте POST запрос на /api/routes.
3. Для получения информации о маршруте отправьте GET запрос на /api/routes/{route_id}.

## Структура проекта

  ```sh
  `api/` - код маршрутизации и приложения.
  `common/` - общие модули и настройки.
  `docker_compose/` - Docker Compose конфигурации.
  `models/` - модели данных.
  `repositories/` - репозитории для работы с данными.
  `services/` - сервисы для логики приложения.
  ```

## Технологии

`FastAPI`
`SQLAlchemy`
`PostgreSQL`
`Pandas`
`Docker`
`Git`
