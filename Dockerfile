FROM tiangolo/uvicorn-gunicorn:python3.9 as dev
ARG USER=fastapi
ENV POETRY_VERSION=1.2.0 \
    POETRY_VIRTUALENVS_CREATE=true
RUN echo $POETRY_VERSION
RUN pip install -U --no-cache-dir pip && \
    pip uninstall -y -r /tmp/requirements.txt && \
    pip install --no-cache-dir "poetry==${POETRY_VERSION}"
RUN useradd -m "${USER}"
USER "${USER}"
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --no-interaction --no-ansi
RUN ln -s $(poetry env info --path) "/home/${USER}/venv"
ENV PATH="/home/${USER}/venv/bin:${PATH}"
COPY ./ /app

FROM tiangolo/uvicorn-gunicorn:python3.9-slim as prod
ARG USER=fastapi
RUN pip install -U --no-cache-dir pip && \
    pip uninstall -y -r /tmp/requirements.txt
RUN useradd -m "${USER}"
USER "${USER}"
COPY --from=dev "/home/${USER}" "/home/${USER}"
ENV PATH="/home/${USER}/venv/bin:${PATH}"
COPY ./ /app
