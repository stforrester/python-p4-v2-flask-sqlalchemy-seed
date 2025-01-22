#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():

    # Create and initialize a faker generator
    fake = Faker()

    # Delete all rows in the "pets" table
    Pet.query.delete()

    # Create an empty list
    pets = []

    # Create a list of set species values that a pet could be
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle', 'Snake', 'Iguana', 'Anteater', 'Ferret', 'Sugar Glider', 'Rat', 'Parrot', 'Parakeet', 'Pidgeon', 'Pig', 'Fish']

    # Add some Pet instances to the list
    for n in range(20):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()