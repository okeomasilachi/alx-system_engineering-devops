#!/usr/bin/python3

"""
using a REST-API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from requests import get
import json


if __name__ == "__main__":
    un = get(f"https://jsonplaceholder.typicode.com/users")
    ut = get(f"https://jsonplaceholder.typicode.com/todos")
    main = {}
    ret_list = [
        {
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        for user in un.json()
        for task in ut.json()
        if user.get("id") == task.get("userId")
    ]

    for user in un.json():
        main[user.get("id")] = [task for task in ret_list
                                if task["username"] == user.get("username")
                                ]

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(main))
