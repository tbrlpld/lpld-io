FROM node:14 as frontend

COPY package.json package-lock.json ./
RUN npm ci --no-optional --no-audit --progress=false

# The whole project is needed to allow purging of the unused CSS classes.
COPY . .
# Compile static files
RUN npm run build:css

FROM python:3.9

RUN mkdir /app
WORKDIR /app
RUN useradd -m lpld -s /bin/bash && \
    chown -R lpld /app

ENV POETRY_HOME=/home/lpld/poetry
ENV PATH=${POETRY_HOME}/bin:$PATH \
    # Ensure dependencies are available globally (without having to mess with the poetry's venvs)
    POETRY_VIRTUALENVS_CREATE=false \
    DJANGO_SETTINGS_MODULE=lpld.settings \
    USE_SQLITE=false
RUN env

# Install litestream (https://litestream.io/install/debian/)
RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.9/litestream-v0.3.9-linux-amd64.deb
RUN dpkg -i litestream-v0.3.9-linux-amd64.deb

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN chown -R lpld:lpld ${POETRY_HOME}

# Install Python dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --no-interaction --no-ansi

USER lpld

COPY --chown=lpld:lpld . .

COPY --chown=lpld:lpld --from=frontend ./lpld/static/comp ./lpld/static/comp

RUN SECRET_KEY=none ./manage.py collectstatic --noinput --clear

EXPOSE 8000
CMD ./scripts/run.sh
