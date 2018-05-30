from sqlalchemy import create_engine
from .models import Pub, Author, Base

engine = create_engine('postgresql+psycopg2://likit:password@localhost/talent_pubdw')

Base.metadata.create_all(engine)


