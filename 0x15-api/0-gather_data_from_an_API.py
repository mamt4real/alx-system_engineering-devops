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


def task_0(userId: str):
    """Print the result of Task 0"""
    user = get_user(userId)
    if user == {}:
        return
    todos = get_todos(userId)
    completed = tuple(filter(
        lambda x: x["completed"], todos
    ))
    name = user["name"]
    print(
        f"Employee {name} is done with tasks({len(completed)}/{len(todos)}):")
    for t in completed:
        print("\t", t["title"])


if __name__ == '__main__':
    try:
        userId = sys.argv[1]
        task_0(userId)
    except IndexError:
        print("Usage: filenae <user_id>")
