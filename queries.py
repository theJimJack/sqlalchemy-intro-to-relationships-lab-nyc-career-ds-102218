from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actors.db')

Session = sessionmaker(bind=engine)
session = Session()


def return_gwyneth_paltrows_roles():
    return session.query(Actor).filter(Actor.name=="Gwyneth Paltrow")[0].roles

def return_tom_hanks_2nd_role():
    return session.query(Actor).filter(Actor.name=="Tom Hanks")[0].roles[1].character
