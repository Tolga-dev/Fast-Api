from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base class
Base = declarative_base()

# Define the Product class mapped to the 'products' table
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)

# Set up the database connection and session
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Add a product
product = Product(name='Laptop', price=999.99)
session.add(product)
session.commit()

