from sqlmodel import SQLModel, Field


class AddressBase(SQLModel):
    street_nr: str
    city: str


class Address(AddressBase, table=True):
    id: int = Field(default=None, primary_key=True)


class AddressCreate(AddressBase):
    pass
