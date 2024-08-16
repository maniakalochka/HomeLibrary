
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()   


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    publication_year = Column(Integer, nullable=True)
    page_count = Column(Integer, nullable=True)
    
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books") 

    def __repr__(self):
        return f"<Book {self.title}>"