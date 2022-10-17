# FastAPI-SQLAlchemy

This is a demo / starter project.

- [Live demo](https://tz-fastapi-sqlalchemy.herokuapp.com/)
- [Documentation](https://tzelleke.github.io/fastapi-sqlalchemy/)

## What is included

- FastAPI
- SQLModel (sits on top of SQLAlchemy)
- Jinja2 (HTML templating for the frontend)

## Local development

```shell
git clone https://github.com/tzelleke/fastapi-sqlalchemy
cd fastapi-sqlalchemy
cp .env-example .env

# will create ./db.sqlite
docker-compose run app alembic upgrade head

# seed database
docker-compose run app inv seed

docker-compose up [-d]
# -> visit localhost:8080
```

## Dependency management

Python package dependencies are managed with [Poetry](https://python-poetry.org/).

## Database

The project uses a SQLite database.
That is, no DB server is involved.
The database DSN is provided via the environment variable `DATABASE_URL` (see `docker-compose.yml`).

The default value, provided in `docker-compose.yml`, is `sqlite:////app/db.sqlite`.
If you run `alembic upgrade head` for the first time it will create `/app/db.sqlite` in the container.
Since the project folder is mapped to `/app` in the container this will create `db.sqlite` in the project folder.

### Migrations

Database schema migrations are managed with [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html).

```shell
# reset database
docker-compose [run | exec] app alembic downgrade base
docker-compose [run | exec] app alembic upgrade head
```

### Seeding

```shell
docker-compose [run | exec] app inv seed
```

## Housekeeping tasks

[pyinvoke](https://docs.pyinvoke.org/en/stable/getting-started.html) is used to run project-related tasks.

## Project documentation

Project documentation is build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

`./github/workflows/ci.yml` defines a workflow to build the documentation on GitHub and publish to GitHub Pages.

You can work on the docs alongside local development.

```shell
# start local docs site
docker-compose up [-d] docs
```

The local `docs` service (see `docker-compose.yml`) is build from `Dockerfile.mkdocs` which installs additional mkdocs extensions into the base image.  
!You have to add these extensions to the GitHub Actions workflow as well.

