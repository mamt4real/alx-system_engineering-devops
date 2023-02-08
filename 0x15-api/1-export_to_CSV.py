#!/usr/bin/python3
"""
Fetch Todos of an Employee using his ID and save in a csv
"""
import requests as req
import sys

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


def task_1(userId: str):
    """Export user tasks to csv"""
    user = get_user(userId)
    if user == {}:
        return
    uname = user.get("username")
    todos = get_todos(userId)
    joined = "\n".join(map(
        lambda t: f'"{userId}","{uname}","{t.get("completed")}","{t.get("title")}"',
        todos
    ))
    with open(f"{userId}.csv", "w") as f:
        f.write(joined + "\n")


if __name__ == '__main__':
    try:
        userId = sys.argv[1]
        task_1(userId)
    except IndexError:
        print("Usage: filenae <user_id>")
