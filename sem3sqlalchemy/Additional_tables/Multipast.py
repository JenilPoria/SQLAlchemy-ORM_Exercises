from sqlalchemy import create_engine, Column, Integer, String, Float
from sem3sqlalchemy.sem3sqlalchemy import Base


class Multipast(Base):
    __tablename__ = "multicast"
    snum = Column(Integer, primary_key=True)
    sname = Column(String)
    city = Column(String)
    comm = Column(Float)

    def __repr__(self):
        return f"<multipast snum={self.snum}, sname={self.sname}, city={self.city}, comm={self.comm}>"