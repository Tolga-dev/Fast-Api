import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('python_web.db')

# Create a cursor object using the cursor() method
cur = conn.cursor()

# SQL command to create the 'users' table
create_users_table = """
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY NOT NULL,
    username TEXT,
    password TEXT
);
"""

# SQL command to create the 'tasks' table
create_tasks_table = """
CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY NOT NULL,
    title TEXT,
    created_at DATETIME,
    is_completed BOOLEAN, 
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id)  -- to define a relationship with the users table
);
"""

# Executing the SQL commands to create the tables
try:
    cur.execute(create_users_table)
    cur.execute(create_tasks_table)
# Committing the changes
    conn.commit()
    print("Tables created successfully.")
except sqlite3.Error as error:
    print("Error occurred while creating tables:", error)
finally:
    # Closing the connection
    cur.close()
    conn.close()

