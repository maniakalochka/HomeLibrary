from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from src.repository.db_config import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True, nullable=False)
    books = relationship("Book", back_populates="author")
