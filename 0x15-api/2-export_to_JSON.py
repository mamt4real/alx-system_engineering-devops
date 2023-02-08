#!/usr/bin/python3
"""
Fetch Todos of an Employee using his ID
"""
import requests as req
import sys
import json

# base url of the api
baseUrl = "https://jsonplaceholder.typicode.com"


def get_todos(userId: str):
    """Fetch All Todos of a User"""
    res = req.get(
        f"{baseUrl}/todos?userId={userId}")
    return res.json()


def get_user(userId: str):
    """Fetch a User"""
    res = req.get(
        f"{baseUrl}/users/{userId}"
    )
    return res.json()


def task_2(userId: str):
    """Export user tasks to json"""
    user = get_user(userId)
    if user == {}:
        return
    uname = user["username"]
    todos = get_todos(userId)
    tasks = list(map(
        lambda t: {
            "task": t["title"],
            "completed": t["completed"],
            "username": uname},
        todos
    ))
    result = {userId: tasks}
    with open(f"{userId}.json", "w") as f:
        f.write(json.dumps(result))


if __name__ == '__main__':
    try:
        userId = sys.argv[1]
        task_2(userId)
    except IndexError:
        print("Usage: filenae <user_id>")
