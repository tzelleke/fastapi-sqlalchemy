# FastAPI-SQLAlchemy

This is a demo / starter project.

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

### Housekeeping tasks

[pyinvoke](https://docs.pyinvoke.org/en/stable/getting-started.html) is used to run project-related tasks.
