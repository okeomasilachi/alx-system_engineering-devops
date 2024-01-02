#!/usr/bin/python3

"""
using a REST-API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from requests import get
from sys import argv


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
        If the `pri` parameter is `True`, print the
            titles of completed tasks.
        If the `pri` parameter is `False`, return a
            tuple containing the number of completed
            tasks (`done`) and the total number of
            tasks (`total`).
    """
    if pri is True:
        for i in data:
            if i.get("completed") is True:
                print("\t ", i.get("title"))
    else:
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
            EMPLOYEE_NAME = un.json().get("name")
            data = ut.json()
            NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS = getTask(data)
            print(f"Employee {EMPLOYEE_NAME} is done with tasks(\
                {NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
            getTask(data, True)
