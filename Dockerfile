FROM python:3.11.4

WORKDIR /src

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true

RUN poetry lock

RUN poetry install --no-root