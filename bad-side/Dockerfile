FROM python:3.9

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_VERSION=1.1.6

RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app
COPY pyproject.toml /app/pyproject.toml
RUN poetry config virtualenvs.create false
RUN export FLASK_APP=main.py
RUN poetry install --no-interaction   
COPY . /app

ENV PATH=./venv:$PATH
CMD flask run