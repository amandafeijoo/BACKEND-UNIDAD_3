FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY musicproject /code/musicproject

CMD ["python3", "musicproject/manage.py", "runserver", "0.0.0.0:8000"]