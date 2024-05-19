from database import engine, session, Base
from models import Product


@staticmethod
def create_table():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.echo = False


@staticmethod
def insert_product(name_, price_, article_):
    with session() as sess:
        res = Product(name=name_,
                      price=price_,
                      article=article_
                      )
        sess.add(res)
        sess.commit()

# create_table()
