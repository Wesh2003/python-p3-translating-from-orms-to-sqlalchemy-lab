from models import Dog
from sqlalchemy import create_engine

def create_table(base,engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()
    #return dogs

def find_by_id(session, id):
    dogs = session.query(Dog).filter(Dog.id == id)
    for i in dogs:
        return i

def find_by_name_and_breed(session, name, breed):
    for dog in session.query(Dog).all():
        if dog.name == name and dog.breed == breed:
            return dog
    
    

def update_breed(session, dog, breed):
    dogs = session.query(Dog).filter(Dog.name == dog).first()
    dogs.breed = breed 
    session.commit()
    return dogs 

