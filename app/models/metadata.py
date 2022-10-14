from sqlmodel import SQLModel

from .address import Address


def get_metadata():
    return SQLModel.metadata
