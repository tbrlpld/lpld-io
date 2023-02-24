# [lpld.io](https://www.lpld.io)

My personal portfolio website.

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

I have now switched to the option to run the frontend tooling in a container.
When you run `docker compose up` the `web` and `frontend` containers are both starting.
Just as with the `web` container, the `frontend` container is just idling after start.
If you want it to do something, you gonna want to open a shell in the container and run the tooling there.

```console
docker compose exec frontend bash
```

Typically, I will I have at least two shells running when working on the frontend.
One is running the web server and one the frontend tooling.
Both are inside their respective containers.

Then, run the tooling in watch mode with:

```console
npm run watch:css
```

If you ever want to build the production ready config, use:

```console
npm run build
```

The production configuration of the frontend assets is build during the container build.
But, when you start the development orchestra as configured in `docker-compose.yml` then the local project directory is mounted into the containers.
This would override the assets in `./lpld/static/comp` that were compiled during image build.
To prevent that from happening, while still allowing the assets build in the `frontend` container to show up in the `web` container, a named volume `frontend_assets` is used.
Only the `frontend` container writes to the volume, while the `web` container reads from it.
With this setup, you don't have to run the frontend tooling if you don't need it, but if you do, the new changes will show up in the `web` container during runtime.

## Deployment

The project contains a `heroku.yml` file for use with Heroku's container deployments.

To get a container deployment runing on Heroku, you need to configure it on the command line (I could not find any way of doing that in the dashboard).

```console
heroku stack:set container -a <app-name>
```

### Configuration

You are going to need to set a few environment variables on the servers.

* `ALLOWED_HOSTS` - Comma separated list of the host domains that the app should be available under.
* `SECRET_KEY` - Salt needed for cryptography in Django. You can generate one with `./manage.py shell -c "from django.utils.crypto import get_random_string; print(get_random_string(50))"`
* `WEB_CONCURRENCY` - Number of worker processes for Gunicorn. You can start with twice the number of processors your server has. On heroku I use 3.

### Static and media files

Static files (CSS, JS) are served by the app with [Whitenoise](https://github.com/evansd/whitenoise).
That means no special settings need to be configured.

Media files need to be uploaded to an S3 bucket though to persist container restarts in hosted environment.
You need to set a couple of environment variables to configure the bucket to use.

* `AWS_S3_ENDPOINT_URL` - Endpoint URL for the bucket including the protocol, e.g. `https://sfo3.digitaloceanspaces.com`.
* `AWS_S3_REGION_NAME` - Region name for the bucket, this information maybe duplicated in the endpoint URL, e.g. `sfo3`.
* `AWS_STORAGE_BUCKET_NAME` - Name of your bucket, e.g. `my-bucket`.
* `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` - Access credentials for the bucket.

### SSL/TLS

Once your app is working, and you have TLS in place, you also configure:

* `SECURE_SSL_REDIRECT=True` - Redirect all requests from `http` to `https`,
* `SECURE_HSTS_SECONDS` - Number of seconds for how long browsers should not retry `http`. This should only be set to a high number after you are sure your configuration works. See also the [Django docs on this](https://docs.djangoproject.com/en/4.1/ref/middleware/#http-strict-transport-security).

### Database

This project is using SQLite as it's database -- even in production 😱.
Using SQLite is often discouraged to be used in production.
Those concerns a usually based on the abilitiy to handle multiple writes and how to backup the database.
For container deployments on a platform as a service (such as Heroku) there is also the problem of persisting the database between container restarts.

The write ability is not really an issue for this application.
Since this app is mainly a content site with few editors working simulaneously (if ever) it is much more read-heavy than write-heavy.
Reads are easy for SQLite to handle.

The persistence problem does apply to this app though.
But, luckily, now there is [Litestream](https://litestream.io/).
Litestream makes it easy to replicate and restore SQLite database to and from persistent storage such as S3.
For the replication and restoration to work you need to create a S3 bucket at some hosting provider and set the following environment variables:

* `DB_DIR` - the directory where the database file `db.sqlite3` is stored locally (it will be created if it does not exist),
* `LITESTREAM_BUCKET_HOST` - the S3 bucket host domain, e.g `my-bucket.nyc3.digitaloceanspaces.com`,
* `LITESTREAM_KEY_ID` and `LITESTREAM_ACCESS_KEY` - the access credentials for the bucket.

The replication is handled in the `./scripts/run.sh` script by wrapping the Gunicorn server process in the Litestream process.
This is the recommended way to [run Litestream in a container](https://litestream.io/guides/docker/).
The restoration is handled in the `./scripts/release.sh` script. This script is run by Heroku on every container restart.

### Scale down Heroku Dynos

Heroku has removed their free plan.
That means having an idle server that is practically not running will start to cost money.
This is a bit of a pain, because I was using the free Dyno for a staging server for my site.
My site is not that important and I could probably do without a staging server, but I like having this stop gap between my local setup and the production one.

It turns out, the paid plans for [Heroku are prorated to the second](https://www.heroku.com/pricing).
I did not know that because I was only running a single paid app and the was on all the time, I never needed any scaling.
But now this becomes interesting.
I hardly need the staging server and I am ok with paying for the few times that I need it.
To not pay the full month for the staging server that I basically never need, I can just scale it down to 0 instances, with:

```console
heroku ps:scale web=0 -a lpld-io-staging
```

If I need to access it, I just need to scale it up again.

```console
heroku ps:scale web=1 -a lpld-io-staging
```

Autoscaling if not an option, because that is only available on the more expensive plans.
But for now I am ok with doing it manually.
