from invoke import task


@task
def seed(c):
    """
    Seed the database with your custom records.
    """
    c.run("python migrations/seed.py")
