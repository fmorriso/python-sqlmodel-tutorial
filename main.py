import sys
from hero import Hero
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy import Engine


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    session = Session(engine)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)

if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    #print(sqlite_url)
    engine: Engine = create_engine(sqlite_url, echo=True)
    #print(type(engine))
    create_db_and_tables()
