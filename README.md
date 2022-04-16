# Westernvalve Website

Website for the Valve company Western Valve

## Local Setup

This project comes with a Docker configuration for local development as well as deployment.

The `Dockerfile` is meant for development as well as production deployment.

The development specific configuration is done via environment variables that are defined in the `docker-compose.yml`.

To start local development, you need to build the required images.

```console
docker compose build
```

That should only be necessary on the first setup.
When you add dependencies, you only want to rebuild the `web` image as otherwise you loose the data in the local development setup.

```console
docker compose build web
```

When the image are build, you can run the containers for the project with:

```console
docker compose up
```

I would suggest to always use `up` and not `start`.
This makes sure that the containers are started with the latest image versions.
I have run into issues (that lead to me messing with configuration for hours) because I did not notice this difference -- basically I was making changes and could not figure out why they are not reflected in the running containers while the build seemed to be influenced correctly.

The `web` container is configured as a busy box in the `docker-compose.yml`.
This means you need to log on to the running container and start the development server manually.

To get onto the container:

```console
docker compose exec web bash
```

Then run the following to start the Django deverlopment server:

```console
./manage.py runserver 0:8000
```

At this point you should be able to connect to the app at `localhost:8000`

I like this setup better (then having the container run the app automatically), because I can always see what is going on with the development process and it allows me to use things like setting breakpoints and jump into the shell.

When you are not using the `docker-compose.yml` configuration, but just use the image build by the `Dockerfile` then the container will start with the production Gunicorn server running.
This is basically what happens on Heroku.


**What about the front-end?**

So far, the front-end tooling only consists of Tailwind CSS.

I am running the front-end tolling locally, not in the container.
That means I have at least two shells running when working on the front-end.

To install the front-end dependencies locally just use `npm`.

```console
npm install
```

Then, run the tooling in watch mode with:

```console
npm run watch:css
```

If you ever want to build the production ready config, use:

```console
npm run build:css
```

The production configuration of the front-end stuff is build during the container build.
But, when you start the development orcestra as configured in `docker-compose.yml` then the local project directory is mounted and overrides what is build in the container.
So you should at least run the production build step once locally.

## Deployment

The project contains a `heroku.yml` file for use with Heroku's container deployments.

To get a container deployment runing on Heroku, you need to configure it on the command line (I could not find any way of doing that in the dashboard).

```console
heroku stack:set container -a <app-name>
```

The project will build and deploy without a database being configured in Heroku.
In that case, it will default to a SQLite database in the container.
That does not make any sense of course, because the database is wiped with every new build.

To connect a database, just add the Heroku Postgres add-on.
When you do that, it should automatically set the `DATABASE_URL` environment variable.
The app settings are configured to then use the connection defined in the `DATABASE_URL` environment variable.
This is done with the `dj-database-url` package.
