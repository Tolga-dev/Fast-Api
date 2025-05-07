from datetime import datetime
from uuid import uuid4

from flask import Flask, make_response, request

app = Flask("TaskManager")

task_storage = {}  # used to store information about tasks


@app.get("/")
def list_tasks():
    tasks = task_storage
    completed_flag = request.args.get("completed", "")  # fetch the query parameter
    if completed_flag.lower() == "true":
        # filter only completed tasks
        tasks = {
            task_id: task_info for task_id, task_info in tasks.items() if task_info["is_completed"]
        }
    elif completed_flag.lower() == "false":
        # filter only not completed tasks
        tasks = {
            task_id: task_info for task_id, task_info in tasks.items() if not task_info["is_completed"]
        }

    return make_response(tasks)  # return tasks


@app.post("/")
def create_task():
    task_id = uuid4().hex  # generate task ID
    task_info = {
        "title": request.json.get("title", "Missed title"),  # get `title` from the request body
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # get current time
        "is_completed": False,  # by default a new task is not completed
    }

    task_storage[task_id] = task_info  # save the task in the storage

    return make_response({"id": task_id})  # return ID of the new task


@app.put("/<task_id>")
def mark_completed(task_id):
    task = task_storage.get(task_id)  # try to find task by the provided ID from the path
    if not task:
        # say to a user that the task with provided ID doesn't exist and provide 404 status code
        return make_response({"message": "Task not found"}, 404)

    task["is_completed"] = True  # mark the task as completed

    return make_response({"is_completed": True})


@app.delete("/<task_id>")
def delete(task_id):
    task = task_storage.pop(task_id, None)  # try to delete task by the provided ID from the path
    if not task:
        # say to a user that the task with provided ID doesn't exist and provide 404 status code
        return make_response({"message": "Task not found"}, 404)

    return make_response({"deleted": True})


if __name__ == "__main__":
    app.run(debug=True)  # run the application in the debug mode

