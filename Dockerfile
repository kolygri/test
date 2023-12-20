FROM python:3.11 as python-base

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR $PYSETUP_PATH
RUN python -m venv $VENV_PATH
RUN . $VENV_PATH/bin/activate
COPY ./pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

WORKDIR /app

COPY . .

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["run.py"]
