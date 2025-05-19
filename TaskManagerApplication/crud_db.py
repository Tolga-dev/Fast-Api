from sqlalchemy import select

import crud_sqlite
import crud_postgresql
from SqlAlchemy.declarativeMapping import Task, User
from db import IS_POSTGRESQL

def is_username_occupied(conn, username):
    if IS_POSTGRESQL:
        user = crud_postgresql.select_user_by_username(conn, username)
    else:
        user = crud_sqlite.select_user_by_username(conn, username)
    return bool(user)

def insert_user(session, user_data):
    # if IS_POSTGRESQL:
    #     return crud_postgresql.insert_user(conn, user_data)
    # else:
    #     return crud_sqlite.insert_user(conn, user_data)
    # 
    username, password = user_data
    user = User(username=username, password=password)
    session.add(user)
    session.commit()


def select_user_by_user_id(conn, user_id):
    if IS_POSTGRESQL:
        return crud_postgresql.select_user_by_user_id(conn, user_id)
    else:
        return crud_sqlite.select_user_by_user_id(conn, user_id)

def select_user_by_username(conn, username):
    if IS_POSTGRESQL:
        return crud_postgresql.select_user_by_username(conn, username)
    else:
        return crud_sqlite.select_user_by_username(conn, username)

def select_user_by_username_password(conn, username, password):
    if IS_POSTGRESQL:
        return crud_postgresql.select_user_by_username_password(conn, username, password)
    else:
        return crud_sqlite.select_user_by_username_password(conn, username, password)

# def insert_task(conn, task_data):
#     if IS_POSTGRESQL:
#         return crud_postgresql.insert_task(conn, task_data)
#     else:
#         return crud_sqlite.insert_task(conn, task_data)

def insert_task(session, task_data):
    title, current_time, is_completed, user_id = task_data
    task = Task(
        title=title,
        created_at=current_time,
        is_completed=is_completed,
        user_id=user_id,
    )
    session.add(task)
    session.commit()
    return task.task_id

def get_completed_tasks(conn, user_id, is_completed):
    if IS_POSTGRESQL:
        return crud_postgresql.get_completed_tasks(conn, user_id, is_completed)
    else:
        return crud_sqlite.get_completed_tasks(conn, user_id, is_completed)

def get_user_tasks(session, user_id):
    tasks = session.execute(
        select(Task).where(Task.user_id == user_id).order_by(Task.created_at, Task.title)
    ).scalars().all()
    return tasks
    # if IS_POSTGRESQL:
    #     return crud_postgresql.get_user_tasks(conn, user_id)
    # else:
    #     return crud_sqlite.get_user_tasks(conn, user_id)

def get_user_task_by_id(conn, user_id, task_id):
    if IS_POSTGRESQL:
        return crud_postgresql.get_user_task_by_id(conn, user_id, task_id)
    else:
        return crud_sqlite.get_user_task_by_id(conn, user_id, task_id)

# def update_task(conn, task_id, title, is_completed):
#     if IS_POSTGRESQL:
#         return crud_postgresql.update_task(conn, task_id, title, is_completed)
#     else:
#         return crud_sqlite.update_task(conn, task_id, title, is_completed)
def update_task(conn, task_id, title, is_completed):
    cur = crud_postgresql.cursor(conn)
    cur.execute('UPDATE tasks SET title=%s, is_completed=%s WHERE task_id=%s', (title, is_completed, task_id))
    conn.commit()

# def delete_task(conn, task_id):
#     if IS_POSTGRESQL:
#         return crud_postgresql.delete_task(conn, task_id)
#     else:
#         return crud_sqlite.delete_task(conn, task_id)
def delete_task(conn, task_id):
    cur = crud_postgresql.cursor(conn)
    cur.execute('DELETE FROM tasks WHERE task_id=%s', (task_id,))
    conn.commit()
