import sys
from hero import Hero
from sqlmodel import create_engine, SQLModel


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    #print(sqlite_url)
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)
