
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Single shared declarative base for the entire schema."""
    pass


