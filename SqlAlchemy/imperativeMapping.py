﻿from sqlalchemy import Table, Column, Integer, ForeignKey, Text, Boolean, DateTime
from sqlalchemy.orm import registry, relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql.ddl import CreateTable

mapper_registry = registry()

users_table = Table(
    "users",
    mapper_registry.metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("username", Text),
    Column("password", Text)
)

class User:
    pass

tasks_table = Table( 
    "tasks",
    mapper_registry.metadata,
    Column("task_id", Integer, primary_key=True, autoincrement=True),
    Column("title", Text),
    Column("created_at", DateTime),
    Column("is_completed", Boolean),
    Column("user_id", Integer, ForeignKey("users.user_id"))
)

class Task:
    pass


mapper_registry.map_imperatively(User, users_table)

mapper_registry.map_imperatively(
    Task,
    tasks_table,
    properties={
        "user_tasks": relationship(User, backref="tasks", order_by=tasks_table.c.user_id)
    },
)


if __name__ == "__main__":
    # Set up the database connection and session

    # For PostgreSQL
    username = 'postgres'
    password = 'postgres'
    host = 'localhost'  # or the IP address of your PostgreSQL server
    port = '5432'  # default PostgreSQL port
    database = 'python_web'
    engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

    # For SQL
    #engine = create_engine("sqlite:///python_web.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create all tables in the database which are defined by mapper registry
    mapper_registry.metadata.create_all(engine)

    print(CreateTable(users_table).compile(engine))
    print(CreateTable(tasks_table).compile(engine))

    # Use SQLAlchemy to add a new product
    user = User(username='Laptop', password="test")

    session.add(user)
    session.commit()
    session.close()

