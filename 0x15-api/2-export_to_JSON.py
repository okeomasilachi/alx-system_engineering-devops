#!/usr/bin/python3

"""
using a REST-API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import json


if __name__ == "__main__":
    if len(argv) >= 2:
        un = get(f"https://jsonplaceholder.typicode.com/users"
                 f"/{argv[1]}")
        ut = get(f"https://jsonplaceholder.typicode.com/users"
                 f"/{argv[1]}/todos")
        if un.status_code == 200:
            UNAME = un.json().get("username")
            data = ut.json()
            with open(f"{data[0].get('userId')}.json", "w",
                      encoding="utf-8") as file:
                main = {}
                ret_list = []
                for i in data:
                    ret_list.append({
                        "task": i.get('title'),
                        "completed": i.get('completed'),
                        "username": UNAME
                        })
                main[i.get('userId')] = ret_list
                file.write(json.dumps(main))
