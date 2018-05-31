import sys
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('postgresql+psycopg2://likit:password@localhost/talent_pubdw')

Session = sessionmaker(bind=engine)
session = Session()


def load_stud_to_db(inputfile, sheetname):
    df = pd.read_excel(inputfile, sheet_name=sheetname)
    total_authors = 0
    for idx, row in df.iterrows():
        if not pd.isna(row['Email']):
            emails = row['Email'].replace(' ', '').split(',')
        else:
            emails = []
        firstname_en = row['FirstNameEn'].lower() if not pd.isna(row['FirstNameEn']) else ''
        lastname_en = row['LastNameEn'].lower() if not pd.isna(row['LastNameEn']) else ''
        firstname_th = row['FirstNameTh'] if not pd.isna(row['FirstNameTh']) else ''
        lastname_th = row['LastNameTh'] if not pd.isna(row['LastNameTh']) else ''
        affil = row['Department'].lower() if not pd.isna(row['Department']) else ''
        country = row['Country'].lower() if not pd.isna(row['Country']) else ''
        field_of_study = row['Major'].lower() if not pd.isna(row['Major']) else ''
        specialty = row['Specialty'].lower() if not pd.isna(row['Specialty']) else ''
        status = True
        degree_title = row['Degree'].lower() if not pd.isna(row['Degree']) else ''

        _degree = session.query(Degree).filter(Degree.title == degree_title).first()
        if not _degree:
            degree = Degree(title=degree_title)
        else:
            degree = _degree

        session.add(degree)

        if firstname_en or lastname_en:
            # search by English name
            _author = session.query(Author).filter(
                        Author.firstname_en == firstname_en,
                        Author.lastname_en == lastname_en).first()
        else:
            # search by Thai name
            _author = session.query(Author).filter(
                Author.firstname_th == firstname_th,
                Author.lastname_th == lastname_th).first()

        if _author:
            print('Author {} {} exists.'.format(_author.firstname_th, _author.lastname_th))
        else:
            new_author = Author(
                firstname_en=firstname_en,
                lastname_en=lastname_en,
                firstname_th=firstname_th,
                lastname_th=lastname_th,
            )
            session.add(new_author)
            session.commit()
            #print('Adding new author {} {}.'.format(new_author.firstname_th, new_author.lastname_th))
            for email in emails:
                _email = session.query(Email).filter(
                            Email.email == email).first()
                if not _email:
                    new_email = Email(email=email)
                    new_author.emails.append(new_email)

            _affil = session.query(Affiliation).filter(Affiliation.name==affil).first()
            if not _affil:
                new_affil = Affiliation(name=affil)
                new_author.affils.append(new_affil)
            else:
                new_author.affils.append(_affil)

            scholarstud = ScholarshipStudent(
                        author_id=new_author.id,
                        country=country,
                        specialty=specialty,
                        field_of_study=field_of_study,
                        status=status,
                        degree_id=degree.id)
            session.add(scholarstud)
            session.commit()
            total_authors += 1
    print(total_authors)


if __name__ == '__main__':
    inputfile = sys.argv[1]
    sheetname = sys.argv[2]
    load_stud_to_db(inputfile, sheetname)

