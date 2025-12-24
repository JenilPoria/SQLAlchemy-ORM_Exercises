from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, Float, Date, Index, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column


engine = create_engine("sqlite:///sem3assignment.db")

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    cnum : Mapped[int] = mapped_column(Integer,primary_key=True)
    cname : Mapped[str] = mapped_column(String(20))
    city : Mapped[str] = mapped_column(String(20))
    rating : Mapped[int] = mapped_column(Integer)
    snum : Mapped[int] = mapped_column(Integer, ForeignKey("salespeople.snum"))

    orders = relationship("Orders", back_populates="customers")

    salesperson = relationship("Salesperson", back_populates="customers")

    def __repr__(self):
        return f"<Customer cnum={self.cnum}, cname={self.cname}, city={self.city}, rating={self.rating}, snum={self.snum}>"


    ## sql_108th_question
    __table_args__ = (
        UniqueConstraint("snum", "rating", name="uq_snum_rating"),
    )

    


class Orders(Base):
    __tablename__ = "order"
    onum : Mapped[int] = mapped_column(Integer,primary_key=True)
    amount : Mapped[float] = mapped_column(Float(10))
    odate : Mapped[Date] = mapped_column(Date)     
    cnum : Mapped[int] = mapped_column(Integer, ForeignKey("customer.cnum"))
    snum : Mapped[int] = mapped_column(Integer, ForeignKey("salespeople.snum"))

    customers = relationship("Customer", back_populates="orders")
    salesperson = relationship("Salesperson", back_populates="orders")


    def __repr__(self):
        return f"<Orders onum={self.onum}, amount={self.amount}, odate={self.odate}, cnum={self.cnum}, snum={self.snum}>"


    ## sql_107th_question
    __table_args__ = (
        Index("idx_orders_snum_odate", "snum", "odate"),
    )


class Salesperson(Base):
    __tablename__ = "salespeople"
    snum : Mapped[int] = mapped_column(Integer,primary_key=True)
    sname : Mapped[str] = mapped_column(String(20))
    city : Mapped[str] = mapped_column(String(20))
    comm : Mapped[float] = mapped_column(Float(10))
    

    customers = relationship("Customer", back_populates="salesperson")
    orders = relationship("Orders", back_populates="salesperson")

    def __repr__(self):
        return f"<Salesperson snum={self.snum}, sname={self.sname}, city={self.city}, comm={self.comm}>"


