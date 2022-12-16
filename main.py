import sqlalchemy as sq
import json
from models import create_tables, Publisher, Book, Shop, Sale, Stock
from sqlalchemy.orm import sessionmaker
import re


if __name__ == '__main__':
    DSN = "postgresql://postgres:1@localhost:5432/books"
    
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open('tests_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(pk=record.get('pk'), **record.get('fields')))
    session.commit()
    
    p_name = input('Введите имя писателя: ')
    
    for q in session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale).\
        join(Publisher).join(Stock).join(Shop).join(Sale).\
            filter(Publisher.name.like(p_name)):
        print(f'{q.title} | {q.name} | {str(q.price * q.count)} | {q.date_sale}')    

    session.close()

