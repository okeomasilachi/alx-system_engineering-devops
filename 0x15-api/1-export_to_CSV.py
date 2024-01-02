#!/usr/bin/python3

"""
using a REST-API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import csv


def getTask(data=[], pri=False):
    """
    print only completed tasks or return the count
    of completed and total tasks,

    Args:
        data: list of dictionaries.
        pri: boolean flag that determines whether to
            print only the completed tasks or return
            the count of completed tasks.

    Returns:
        tuple containing the number of completed
        tasks (`done`) and the total number of
        tasks (`total`).
    """
    done = 0
    total = len(data)
    if not data:
        return (done, total)
    for i in data:
        if i.get("completed") is True:
            done += 1
    return (done, total)


if __name__ == "__main__":
    if len(argv) >= 2:
        un = get(f"https://jsonplaceholder.typicode.com/users"
                 f"/{argv[1]}")
        ut = get(f"https://jsonplaceholder.typicode.com/users"
                 f"/{argv[1]}/todos")
        if un.status_code == 200:
            UNAME = un.json().get("username")
            data = ut.json()
            with open(f"{data[0].get('userId')}.csv", "w",
                      encoding="utf-8") as file:
                wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                for i in data:
                    wr.writerow([
                        i.get('userId'),
                        UNAME,
                        i.get('completed'),
                        i.get('title')
                        ]
                    )
