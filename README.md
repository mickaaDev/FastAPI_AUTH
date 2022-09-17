Description:

The web server is designed to authorize the user via API, authorized
use create model Image
(Not finished: image generation, tests, Nginx)


Stack:

    Python 
    FastAPI 
    SQLAlchemy
    Pydantic
    Email_Validator
    uvicorn
    PyJWT
    python-multipart


Start: 
First step clone the repository

    git clone https://github.com/Nurmanbetov/FastAPI_AUTH.git

Create an environment for libraries

    python3 -m venv venv

Activate the environment

    source venv/bin/activate

Install all libraries from req.txt folder

    pip install -r req.txt

Create an image

    docker-compose build

Run container

    docker-compose up

Go to address

    http://127.0.0.1:8000/docs





