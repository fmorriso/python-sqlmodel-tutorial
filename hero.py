from typing import Optional

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    # in this context, Optional[int] means "we won't generate the value, the database will do that for us.
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    # in this context, Optional[int] means an instance of this class can be created without specifying a value for age.
    age: Optional[int] = None
