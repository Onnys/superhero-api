from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


database_name = 'superhero'
database_path = "postgres://{}:{}@{}/{}".format('superhero','hero','localhost:5432', database_name)
db = SQLAlchemy()

def setup_db(app, database_path= database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    # db.create_all()


class superheros(db.Model):
    __tablename__ = 'superheros'
    id = Column (Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    #powerstats
    intelligence = Column(Integer)
    strength = Column(Integer)
    speed = Column(Integer)
    durability = Column(Integer)
    power = Column(Integer)
    combat = Column(Integer)
    # appearance
    gender = Column(String)
    race = Column(String)
    height = Column(db.ARRAY(String))
    weight = Column(db.ARRAY(String))
    eyeColor = Column(String)
    hairColor = Column(String)
    # biography
    fullName = Column(String)
    alterEgos = Column(String)
    aliases = Column(db.ARRAY(String))
    placeOfBirth = Column(String)
    firstAppearance = Column(String)
    publisher = Column(String)
    alignment = Column(String)
    # work
    occupation = Column(String)
    base = Column(String)
    # connections
    groupAffiliation = Column(String)
    relatives = Column(String)
    # images
    xs = Column(String)
    sm = Column(String)
    md = Column(String)
    lg = Column(String)

    def __init__(self, name, slug, intelligence, strength, speed, durability,power, combat, gender,race, height, weight, eyeColor, hairColor, fullName, alterEgos, aliases, placeOfBirth, firstAppearance, publisher, alignment, occupation, base, groupAffiliation, relatives, xs, sm, md,lg):
        self.name = name
        self.slug = slug
        self.intelligence = intelligence
        self.strength = strength
        self.speed = speed
        self.durability = durability
        self.power = power
        self.combat = combat
        self.gender = gender
        self.race = race
        self.height = height
        self.weight = weight
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.fullName = fullName
        self.alterEgos = alterEgos
        self.aliases = aliases
        self.placeOfBirth = placeOfBirth
        self.firstAppearance = firstAppearance
        self.publisher = publisher
        self.alignment = alignment
        self.occupation = occupation
        self.base = base
        self.groupAffiliation = groupAffiliation
        self.relatives = relatives
        self.xs = xs
        self.sm = sm
        self.md = md
        self.lg = lg

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
         return {
             'id': self.id,
             'name': self.name,
             'slug': self.slug,
             'powerstats': {
                 'intelligence': self.intelligence,
                 'strength': self.strength,
                 'speed': self.speed,
                 'durability': self.durability,
                 'power': self.power,
                 'combat': self.combat,
             },
             'appearance':{
                 'gender': self.gender,
                 'race': self.race,
                 'height': self.height,
                 'weight': self.weight,
                 'eyeColor': self.eyeColor,
                 'hairColor': self.hairColor,
             },
             'biography': {
                 'fullName': self.fullName,
                 'alterEgos': self.alterEgos,
                 'aliases': self.aliases,
                 'placeOfBirth': self.placeOfBirth,
                 'firstAppearance': self.firstAppearance,
                 'publisher': self.publisher,
                 'alignment': self.alignment,
             },
             'work': {
                 'occupation': self.occupation,
                 'base': self.base,
             },
             'connections':{
                 'groupAffiliation': self.groupAffiliation,
                 'relatives': self.relatives,
             },
             'images':{
                 'xs': self.xs,
                 'sm': self.sm,
                 'md': self.md,
                 'lg':self.lg,
             }
         }
    # def powerstats(self):
    #     return {

    #     }
