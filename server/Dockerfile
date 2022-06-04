FROM python:3.9-slim-buster

EXPOSE 5000

WORKDIR /app

COPY ./requirements.txt /app
COPY ./server.py /app

RUN python -m pip install -r requirements.txt

CMD ["python", "server.py"]