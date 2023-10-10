FROM node:18-bookworm-slim as frontend

WORKDIR /home/node/app

COPY package.json package-lock.json ./
RUN npm ci --no-optional --no-audit --progress=false

# The whole project is needed to allow purging of the unused CSS classes.
COPY . .
# Compile static files
RUN npm run build

FROM python:3.11 as backend-production

RUN mkdir /app && mkdir /data
RUN useradd -m lpld -s /bin/bash && \
    chown -R lpld /app && \
    chown -R lpld /data
WORKDIR /app

# Enable Heroku Exec: https://devcenter.heroku.com/articles/exec#using-with-docker
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    apt update -y && apt install -y iproute2 openssh-server

ENV POETRY_HOME=/home/lpld/poetry
ENV PATH=${POETRY_HOME}/bin:$PATH \
    # Ensure dependencies are available globally (without having to mess with the poetry's venvs)
    POETRY_VIRTUALENVS_CREATE=false \
    DJANGO_SETTINGS_MODULE=lpld.settings \
    SQLITE_FILE=/data/db.sqlite3 \
    PORT=8000
RUN env

# Install litestream (https://litestream.io/install/debian/)
ARG PLATFORM=amd64
RUN wget https://github.com/benbjohnson/litestream/releases/download/v0.3.9/litestream-v0.3.9-linux-$PLATFORM.deb
RUN dpkg -i litestream-v0.3.9-linux-$PLATFORM.deb

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN chown -R lpld:lpld ${POETRY_HOME}

# Install Python dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-root --no-interaction --no-ansi --without dev

USER lpld

COPY --chown=lpld:lpld . .

COPY --chown=lpld:lpld --from=frontend /home/node/app/lpld/static/comp /app/lpld/static/comp

RUN SECRET_KEY=none ./manage.py collectstatic --noinput --clear

EXPOSE 8000
CMD ./scripts/run.sh


FROM backend-production AS backend-development

USER root

RUN poetry install --no-root --no-interaction --no-ansi --with dev

USER lpld
