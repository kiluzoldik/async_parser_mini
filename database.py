from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

engine = create_engine(
    url='sqlite:///data.db',
    echo=True
)

session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
