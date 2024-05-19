from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[float]
    article: Mapped[str]
