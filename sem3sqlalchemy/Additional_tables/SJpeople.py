from sqlalchemy import Column, Integer, String, Float
from sem3sqlalchemy.sem3sqlalchemy import Base


class Sjpeople(Base):
    __tablename__ = 'SJpeople'  # Must match the table name in DB
    snum = Column(Integer, primary_key=True)
    sname = Column(String)
    city = Column(String)
    comm = Column(Float)

    def __repr__(self):
        return f"<Sjpeople snum={self.snum}, sname={self.sname}, city={self.city}, comm={self.comm}>"
