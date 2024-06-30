
# RESTful API для управления списком задач (TODO list) на Flask

Данный проект представляет собой веб-приложение на Flask, которое предоставляет RESTful API для управления списком задач (TODO list).

## Функциональность

Приложение включает в себя следующие возможности:

1. **Создание задачи**:
   - Метод: POST
   - URL: /tasks
   - Параметры запроса: JSON-объект с полями title (строка) и description (строка, опционально).
   - Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

2. **Получение списка задач**:
   - Метод: GET
   - URL: /tasks
   - Ответ: JSON-список задач, где каждая задача представляет собой JSON-объект с полями id, title, description, created_at, updated_at.

3. **Получение информации о задаче**:
   - Метод: GET
   - URL: /tasks/<id>
   - Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

4. **Обновление задачи**:
   - Метод: PUT
   - URL: /tasks/<id>
   - Параметры запроса: JSON-объект с полями title (строка, опционально) и description (строка, опционально).
   - Ответ: JSON-объект с полями id, title, description, created_at, updated_at.

5. **Удаление задачи**:
   - Метод: DELETE
   - URL: /tasks/<id>
   - Ответ: Сообщение об успешном удалении.

## Требования

1. Flask
2. MySQL
3. Python 3.x

## Установка и запуск

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/VehsagriX/Todotasks.git
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Настройте подключение к базе данных MySQL в файле `config.py`.

4. Создайте таблицу в базе данных. Можно воспользоваться скриптом `create_tables.sql`:

   ```bash
   mysql -u username -p database_name < create_tables.sql
   ```

5. Запустите приложение:

   ```bash
   python app.py
   ```

## Использование

Вы можете использовать любой HTTP-клиент, такой как Postman или curl, для отправки запросов к API.

Примеры запросов:

- Создание задачи:

  ```bash
  curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Новая задача", "description": "Описание новой задачи"}'
  ```

- Получение списка задач:

  ```bash
  curl http://localhost:5000/tasks
  ```

- Получение информации о задаче:

  ```bash
  curl http://localhost:5000/tasks/1
  ```

- Обновление задачи:

  ```bash
  curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"title": "Измененное название задачи"}'
  ```

- Удаление задачи:

  ```bash
  curl -X DELETE http://localhost:5000/tasks/1
  ```


