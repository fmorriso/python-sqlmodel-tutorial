import sys
from hero import Hero
from sqlmodel import create_engine, SQLModel
from sqlalchemy import Engine


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    #print(sqlite_url)
    engine: Engine = create_engine(sqlite_url, echo=True)
    #print(type(engine))
    create_db_and_tables()
