#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_obj = session.query(State).order_by(State.id).first()
    if first_obj is None:
        print("Nothing")
    else:
        print(f"{first_obj.id}: {first_obj.name}")
