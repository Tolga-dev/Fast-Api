from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from LearningFastApi.config import Settings

SQLALCHEMY_DATABASE_URI = f'postgresql://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}/{Settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db =  session_local()
    try:
        yield db
    finally:
        db.close()

# 
# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='postgres', user='postgres', password='Postgre', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected to PostgreSQL")
#         break
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#         time.sleep(2)
