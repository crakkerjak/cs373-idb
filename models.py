# sample from docs:
# http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
from sqlalchemy import Column, String, Integer
from database import Base
from flask_sqlalchemy import sqlalchemy

db = SQLAlchemy()


class Cocktail(Base):
    """Cocktail model.

    Contains cocktail attributes and a one-to-many relationship to Ingredients

    Attributes:
        __tablename__: A string, the database table name.
        id_: An integer representing primary key sequence.
        name: A string. The name of the cocktail.
        glass: A string indicating the recommended glass for consumption.
        ingredients: One-to-many relationship with ingredients objects.
        recipe: A string with directions to make the cocktail.
        image: A string indicating the folder/filename for a static image.
    """
    __tablename__ = 'cocktails'
    id_ = Column(Integer, primary_key=True)
    name = Column(String(50), primary_key=True)
    glass = Column(String(50))
    ingredients = db.relationship('Ingredient', backref='cocktail',
                                  lazy='dynamic')
    recipe = Column(String(1024))
    image = Column(String(128))

    def __init__(self, name, glass, recipe, image=None):
        self.name = name
        self.glass = glass
        self.recipe = recipe
        self.image = image

    def __repr__(self):
        return '<Cocktail %r>' % (self.name)


class Ingredient(Base):
    """Ingerdient model.

    Contains cocktail attributes and a one-to-many relationship to Ingredients

    Attributes:
        __tablename__: A string, the database table name.
        id_: An integer representing primary key sequence.
        name: A string. The name of the cocktail.
        glass: A string indicating the recommended glass for consumption.
        ingredients: One-to-many relationship with ingredients objects.
        recipe: A string with directions to make the cocktail.
        image: A string indicating the folder/filename for a static image.
    """
    __tablename__ = 'ingredients'
    id_ = Column(Integer, primary_key=True)
    name = Column(String(50))
    amount = Column(String(50))
    image = Column(String(128))

    def __init__(self, name, amount=None, image=None):
        self.name = name
        self.amount = amount
        self.image = image

    def __repr__(self):
        return '<Ingredient %r>' % (self.name)
