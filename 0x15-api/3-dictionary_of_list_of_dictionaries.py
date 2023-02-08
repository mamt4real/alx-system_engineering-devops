#!/usr/bin/python3
"""
Fetch Todos of all Employees
"""
import requests as req
import json

# base url of the api
baseUrl = "https://jsonplaceholder.typicode.com"


def get_todos(userId: str):
    """Fetch All Todos of a User"""
    res = req.get(
        f"{baseUrl}/todos?userId={userId}")
    return res.json()


def get_users():
    """Fetch all Users"""
    res = req.get(
        f"{baseUrl}/users"
    )
    return res.json()


def link_user_with_todos(user: dict):
    """Link a user with his todos"""
    if user == {}:
        return
    userId = user["id"]
    uname = user["username"]
    todos = get_todos(userId)
    tasks = list(map(
        lambda t: {
            "username": uname,
            "task": t["title"],
            "completed": t["completed"]},
        todos
    ))
    result = {userId: tasks}
    return result


def task_3():
    """Save all users with their tasks in a json format"""
    result = {}
    for user in get_users():
        result.update(link_user_with_todos(user))
    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(result))


if __name__ == '__main__':
    task_3()
