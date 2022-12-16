import sqlalchemy as sq
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class Publisher(Base):
    __tablename__ = 'publisher'

    pk = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)
    books = relationship('Book', backref='publisher')

    def __str__(self):
        return [self.pk, self.name]

class Book(Base):
    __tablename__ = 'book'

    pk = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.pk"), nullable=False)

    def __str__(self):
        return [self.pk, self.title, self.id_publisher]

class Shop(Base):
    __tablename__ = 'shop'

    pk = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        return [self.pk, self.name]

class Stock(Base):
    __tablename__ = 'stock'

    pk = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.pk"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.pk"), nullable=False)
    count = sq.Column(sq.Integer)
    sales = relationship('Sale', backref='sale')
    books = relationship('Book', backref='book')

    def __str__(self):
        return [self.pk, self.id_book, self.id_shop, self.count]


class Sale(Base):
    __tablename__ = 'sale'

    pk = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.String)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.pk"), nullable=False)
    count = sq.Column(sq.Integer)

    def __str__(self):
        return [self.pk, self.price, self.date_sale, self.count, self.id_stock]



