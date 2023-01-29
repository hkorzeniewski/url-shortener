FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /code
WORKDIR /code
RUN pip3 install poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-root

COPY . /code/

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]