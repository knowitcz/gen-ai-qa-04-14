from sqlmodel import SQLModel, Field

class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    balance: int
    type: str
