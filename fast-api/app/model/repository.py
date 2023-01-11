from sqlalchemy import delete, insert, select, update

from app.model.connection import Session
from app.model.tables import ExampleDatabase


class ExampleRepository:

    def create(self, data):
        with Session() as session, session.begin():
            session.execute(insert(ExampleDatabase).values(data))

    def read(self):
        with Session() as session:
            result: list[ExampleDatabase] = session.execute(
                select(ExampleDatabase)
            ).scalars().all()

            return result

    def update(self, id, data):
        with Session() as session, session.begin():
            session.execute(
                update(ExampleDatabase).values(data)
                .where(ExampleDatabase.id == id)
            )

    def delete(self, id):
        with Session() as session, session.begin():
            session.execute(
                delete(ExampleDatabase).where(ExampleDatabase.id == id)
            )
