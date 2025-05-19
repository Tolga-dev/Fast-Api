import psycopg2
from psycopg2 import sql

# Database connection parameters
dbname = 'python_web'
user = 'postgres'
password = 'postgre'
host = 'localhost'


# SQL statements to create tables
create_users_table = """
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);
"""

create_tasks_table = """
CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    title TEXT,
    created_at TIMESTAMP,
    is_completed BOOLEAN, 
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
"""

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()

# Execute SQL commands to create tables
try:
    cur.execute(create_users_table)
    cur.execute(create_tasks_table)
    conn.commit()  # Commit changes to the database
    print("Tables created successfully")
except Exception as e:
    print("Error occurred while creating tables:", e)
    conn.rollback()  # Rollback changes on error
finally:
    cur.close()  # Close the cursor
    conn.close()  # Close the connection
