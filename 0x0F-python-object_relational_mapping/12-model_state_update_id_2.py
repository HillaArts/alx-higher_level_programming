#!/usr/bin/python3
"""
script that changes the name of a state object
from the database
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    change the name of a state object
    """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    update_state = session.query(State).filter(State.id == '2').first()
    update_state.name = 'New Mexico'
    session.commit()
    session.close()
