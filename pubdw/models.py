from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, Boolean
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

AuthorAffilTable = Table('author_affil_table', Base.metadata,
                         Column('author_id', Integer, ForeignKey('authors.id')),
                         Column('affil_id', Integer, ForeignKey('affils.id'))
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
                           secondary=AuthorEmailTable,
                           backref='authors')
    affils = relationship('Affiliation',
                          secondary=AuthorAffilTable,
                          backref='authors')


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer(), primary_key=True)
    email = Column(String())


class Degree(Base):
    __tablename__ = 'degrees'
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)
    level = Column(Integer())


class ScholarshipStudent(Base):
    __tablename__ = 'scholarship_students'
    id = Column(Integer(), primary_key=True)
    author_id = Column(Integer(), ForeignKey('authors.id'))
    country = Column(String())
    status = Column(Boolean())
    field_of_study = Column(String())
    specialty = Column(String())
    degree_id = Column(Integer(), ForeignKey('degrees.id'))


class Affiliation(Base):
    __tablename__ = 'affils'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    city = Column(String())
