from sem3sqlalchemy import Customer, Orders, Salesperson, engine, Base
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, Float, Date, insert
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column
from datetime import date


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


customer_entries = insert(Customer).values([
    {"cnum": 2001, "cname": "Hoffman", "city": "London", "rating": 100, "snum": 1001},
    {"cnum": 2002, "cname": "Glovanne", "city": "Rome", "rating": 200, "snum": 1003},
    {"cnum": 2003, "cname": "Liu", "city": "San Jose", "rating": 300, "snum": 1002},
    {"cnum": 2004, "cname": "Grass", "city": "Berlin", "rating": 100, "snum": 1002},
    {"cnum": 2006, "cname": "Clemens", "city": "London", "rating": 300, "snum": 1007},
    {"cnum": 2007, "cname": "Pereira", "city": "Rome", "rating": 100, "snum": 1004}

])

# session.execute(customer_entries)
# session.commit()


order_entries = insert(Orders).values([
    {"onum": 3001, "amount": 18.69, "odate": date(2016, 3, 10), "cnum": 2003, "snum": 1007},
    {"onum": 3003, "amount": 767.19, "odate": date(2016, 3, 10), "cnum": 2001, "snum": 1001},
    {"onum": 3002, "amount": 1800.1, "odate": date(2016, 3, 10), "cnum": 2002, "snum": 1004},
    {"onum": 3005, "amount": 5160.45, "odate": date(2016, 3, 10), "cnum": 2003, "snum": 1002},
    {"onum": 3006, "amount": 1098.16, "odate": date(2016, 3, 10), "cnum": 2003, "snum": 1007},
    {"onum": 3009, "amount": 1713.23, "odate": date(2016, 4, 10), "cnum": 2002, "snum": 1003},
    {"onum": 3007, "amount": 75.75, "odate": date(2016, 4, 10), "cnum": 2004, "snum": 1002},
    {"onum": 3008, "amount": 4723, "odate": date(2016, 5, 10), "cnum": 2006, "snum": 1001},
    {"onum": 3010, "amount": 1309.95, "odate": date(2016, 6, 10), "cnum": 2004, "snum": 1002},
    {"onum": 3011, "amount": 8891.78, "odate": date(2016, 6, 10), "cnum": 2006, "snum": 1001}
])

# session.execute(order_entries)
# session.commit()

salesperson_entries = insert(Salesperson).values([
    {"snum": 1001, "sname": "Peel", "city": "London", "comm": 0.12},
    {"snum": 1002, "sname": "Serres", "city": "San Jose", "comm": 0.13},
    {"snum": 1004, "sname": "Motika", "city": "London", "comm": 0.11},
    {"snum": 1007, "sname": "Rifkin", "city": "Barcelona", "comm": 0.15},
    {"snum": 1003, "sname": "Axelrod", "city": "New York", "comm": 0.10}
])

# session.execute(salesperson_entries)
# session.commit()