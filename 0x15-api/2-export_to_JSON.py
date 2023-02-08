#!/usr/bin/python3
"""
Fetch Todos of an Employee using his ID and save in a json file
"""
import json
import requests as req
import sys

# base url of the api
baseUrl = "https://jsonplaceholder.typicode.com"


def get_todos(userId: str):
    """Fetch All Todos of a User"""
    res = req.get(
        "{}/todos?userId={}".format(baseUrl, userId))
    return res.json()


def get_user(userId: str):
    """Fetch a User"""
    res = req.get(
        "{}/users/{}".format(baseUrl, userId)
    )
    return res.json()


def task_2(userId: str):
    """Export user tasks to json"""
    user = get_user(userId)
    if user == {}:
        return
    uname = user.get("username")
    todos = get_todos(userId)
    tasks = list(map(
        lambda t: {
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": uname},
        todos
    ))
    result = {userId: tasks}
    with open("{}.json".format(userId), "w") as f:
        f.write(json.dumps(result))


if __name__ == '__main__':
    try:
        userId = sys.argv[1]
        task_2(userId)
    except IndexError:
        print("Usage: filenae <user_id>")
