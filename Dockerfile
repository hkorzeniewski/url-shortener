FROM python:3.10

RUN mkdir /code
WORKDIR /code

RUN poetry init
RUN poetry install