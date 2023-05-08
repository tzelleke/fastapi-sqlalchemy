from faker import Faker

from app.db import get_session
from app.models.address import Address

fake = Faker()


def seed_address_table(n):
    global fake
    session = next(get_session())
    print(f"Seeding {Address} data.")
    for _ in range(n):
        session.add(
            Address(
                street_nr=fake.street_address(),
                city=fake.city(),
            )
        )
    session.commit()
    print(f"Seeded {Address} data.")


if __name__ == "__main__":
    seed_address_table(25)
