from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

PubAuthorTable = Table('pub_author_table', Base.metadata,
                       Column('pub_id', Integer, ForeignKey('pubs.id')),
                       Column('author_id', Integer, ForeignKey('authors.id'))
                       )

AuthorEmailTable = Table('author_email_table', Base.metadata,
                       Column('author_id', Integer, ForeignKey('authors.id')),
                       Column('email_id', Integer, ForeignKey('emails.id'))
                       )


class Pub(Base):
    __tablename__ = 'pubs'
    id = Column(Integer(), primary_key=True)
    doi = Column(String(), unique=True)
    title = Column(String(), index=True)
    abstract = Column(String())
    pub_date = Column(Date())
    citation_count = Column(Integer())
    detail = Column(JSON())
    authors = relationship('Author',
                            secondary=PubAuthorTable,
                            backref='publications')


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer(), primary_key=True)
    firstname_en = Column(String())
    lastname_en = Column(String())
    firstname_th = Column(String())
    lastname_th = Column(String())
    emails = relationship('Email',
                           secondary=PubAuthorTable,
                           backref='authors')


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer(), primary_key=True)
    email = Column(String())
