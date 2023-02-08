#!/usr/bin/python3
"""Using a public API 'https://jsonplaceholder.typicode.com'"""
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


def task_0(userId: str):
    """Print the result of Task 0"""
    user = get_user(userId)
    if user == {}:
        return
    todos = get_todos(userId)
    completed = tuple(filter(
        lambda x: x["completed"], todos
    ))
    name = user.get("name")
    print(
        "Employee {} is done with tasks({}/{}):".format(
            name, len(completed), len(todos)
        ))
    for t in completed:
        print("\t", t.get("title"))


if __name__ == '__main__':
    try:
        userId = sys.argv[1]
        task_0(userId)
    except IndexError:
        print("Usage: filenae <user_id>")
