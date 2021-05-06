FROM python:3.9

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.6 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" 


RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /app
COPY pyproject.toml /app/pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction   
COPY . /app

ENV PATH=./venv:$PATH
ENV FLASK_APP=/app/main.py
ENV FLASK_ENV=development
EXPOSE 8000
CMD ["flask" ,"run", "--host=0.0.0.0", "--port=8000"]