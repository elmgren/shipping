FROM tiangolo/uvicorn-gunicorn:python3.9-slim AS prepare
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
		libpq-dev \
		python-dev \
		build-essential

RUN pip install --no-cache-dir poetry

WORKDIR /app
COPY poetry.lock /app
COPY pyproject.toml /app
RUN poetry config virtualenvs.in-project true \
	&& poetry install --no-dev --no-interaction --extras "gunicorn"

FROM tiangolo/uvicorn-gunicorn:python3.9-slim
ENV PATH=/app/.venv/bin:${PATH}

RUN apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y libpq5

COPY --from=prepare /app/.venv /app/.venv
COPY alembic.ini /app/
COPY alembic /app/alembic/
COPY app/ app/
