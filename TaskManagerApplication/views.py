﻿from datetime import datetime
from uuid import uuid4

from flask import Blueprint, make_response, request

from db import task_storage

bp = Blueprint("tasks", __name__)


@bp.get("/")
def list_tasks():
    completed_flag = request.args.get("completed")  # fetch the query parameter
    # check that query parameter has valid value
    if completed_flag and completed_flag.lower() not in ("true", "false"):
        return make_response(
            {"message": "Wrong value for `completed`. Expected `true` or `false`."},
            400,
        )

    flag_mapping = {"true": True, "false": False}

    if not completed_flag:
        # return all tasks if query parameter was not provided
        tasks = task_storage
    else:
        # filter only not completed tasks
        tasks = {
            task_id: task_info for task_id, task_info in task_storage.items()
            if task_info["is_completed"] == flag_mapping[completed_flag.lower()]
        }

    return make_response(tasks)  # return tasks


@bp.post("/")
def create_task():
    task_id = uuid4().hex  # generate task ID
    task_info = {
        "title": request.json.get("title", "Missed title"),  # get `title` from the request body
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # get current time
        "is_completed": False,  # by default a new task is not completed
    }

    task_storage[task_id] = task_info  # save the task in the storage

    return make_response({"id": task_id})  # return ID of the new task


@bp.put("/<task_id>")
def mark_completed(task_id):
    task = task_storage.get(task_id)  # try to find task by the provided ID from the path
    if not task:
        # say to a user that the task with provided ID doesn't exist and provide 404 status code
        return make_response({"message": "Task not found"}, 404)

    task["is_completed"] = True  # mark the task as completed

    return make_response({"is_completed": True})


@bp.delete("/<task_id>")
def delete(task_id):
    task = task_storage.pop(task_id, None)  # try to delete task by the provided ID from the path
    if not task:
        # say to a user that the task with provided ID doesn't exist and provide 404 status code
        return make_response({"message": "Task not found"}, 404)

    return make_response({"deleted": True})

 