from sqlalchemy import create_engine, Column, Integer, String, Float
from sem3sqlalchemy.sem3sqlalchemy import Base
from sqlalchemy.orm import sessionmaker


class LondonStaff(Base):
    __tablename__ = 'LondonStaff'  # Must match the table name in DB
    snum = Column(Integer, primary_key=True)
    sname = Column(String)
    city = Column(String)
    comm = Column(Float)

    def __repr__(self):
        return f"<londonStaff snum={self.snum}, sname={self.sname}, city={self.city}, comm={self.comm}>"
