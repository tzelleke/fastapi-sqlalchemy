from sqlmodel import SQLModel

from .address import Address  # noqa: F401


def get_metadata():
    return SQLModel.metadata
