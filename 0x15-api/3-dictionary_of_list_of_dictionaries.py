#!/usr/bin/python3
# Testing how to fetch data grom an API
"""
Fetch Todos of all Employees
"""
import json
import requests as req

# base url of the api
baseUrl = "https://jsonplaceholder.typicode.com"


def get_todos(userId: str):
    """Fetch All Todos of a User"""
    res = req.get(
        "{}/todos?userId={}".format(baseUrl, userId))
    return res.json()


def get_users():
    """Fetch all Users"""
    res = req.get(
        "{}/users".format(baseUrl)
    )
    return res.json()


def link_user_with_todos(user: dict):
    """Link a user with his todos"""
    if user == {}:
        return
    userId = user.get("id")
    uname = user.get("username")
    todos = get_todos(userId)
    tasks = list(map(
        lambda t: {
            "username": uname,
            "task": t.get("title"),
            "completed": t.get("completed")},
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
