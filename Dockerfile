FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
WORKDIR /app/
ENV POETRY_VERSION=1.2.0 \
    POETRY_VIRTUALENVS_CREATE=false
RUN pip install -U pip && \
    pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi
COPY ./ /app
ENV PYTHONPATH=/app