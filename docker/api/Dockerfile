ARG VERSION

FROM python:${VERSION} as requirements-stage

WORKDIR /src

RUN pip install poetry

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /src

RUN poetry build

FROM python:${VERSION}

COPY --from=requirements-stage /src/dist/ /tmp/dist

RUN pip install --no-cache-dir --upgrade $(ls /tmp/dist/*.whl)

CMD ["uvicorn", "fullstack_todo.api:app", "--host", "0.0.0.0", "--port", "80"]