#!/usr/bin/python3
""" For a given employee, returns information about the TODO list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    except IndexError:
        exit

    res = requests.get(url)
    res = res.json()
    user_deets = "Employee {} is done with tasks".format(res.get('name'))
    print(user_deets, end="")
    res = requests.get(url + "/todos")
    res = res.json()
    done = 0
    for task in res:
        if task.get('completed'):
            done += 1
    print("({}/{}):".format(done, len(res)))
    [print("\t {}".format(task.get('title')))
        if task.get('completed') else "" for task in res]
