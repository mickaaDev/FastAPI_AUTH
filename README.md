Описание:

Веб-сервер предназначен для авторизации пользователя по API, авторизованные 
пользователи могут создать модель Image
(Не закончено: генерация изображения, тесты, Nginx)


Стек:

    Python 
    FastAPI 
    SQLAlchemy
    Pydantic
    Email_Validator
    uvicorn
    PyJWT
    python-multipart


Старт: 

Первый шаг сколнировать репозитрий

    git clone https://github.com/Nurmanbetov/FastAPI_AUTH.git
Создать инвайромент для библеотек
 
    python3 -m venv venv

Активировать инвайромент

    source venv/bin/activate

Установить все библеотеки с папки req.txt

    pip install -r req.txt

Создать образ

    docker-compose build

Запустить контейнер

    docker-compose up

Перейти по адресу

    http://127.0.0.1:8000/docs





