FROM python:3.9-alpine

WORKDIR /usr/src/app
ADD req.txt .

RUN pip install -r req.txt

CMD [ "uvicorn", "main:apps", "--reload", "--host", "0.0.0.0", "--port", "8000"]
