from sqlalchemy import Column, Integer, String, Float
from sem3sqlalchemy.sem3sqlalchemy import Base


class Bonus(Base):
    __tablename__ = "bonus"
    snum = Column(Integer, primary_key=True)
    odate = Column(String)
    amount = Column(Integer)

    def __repr__(self):
        return f"<bonus snum={self.snum}, odate={self.odate}, amount={self.amount}>"