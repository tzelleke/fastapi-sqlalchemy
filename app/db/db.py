from typing import Iterator

from sqlmodel import create_engine, Session

from app.core.config import DATABASE_URL

# from app.core.logging import logger

engine = create_engine(
    DATABASE_URL, echo=True, connect_args=dict(check_same_thread=False),
)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
