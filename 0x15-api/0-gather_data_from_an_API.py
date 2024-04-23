#!/usr/bin/python3
"""
Gather data from an API
Queries 'https://jsonplaceholder.typicode.com/' for a given employee ID
Return employee information
"""
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'


def get_tasks(employee_id):
    """Get the tasks of the employee."""
    resp = requests.get(f"{API_URL}/users/{employee_id}/todos")
    if resp:
        return resp.json()
    return {}


def get_employee_name(employee_id):
    """Get the name of the employee."""
    resp = requests.get(f"{API_URL}/users/{employee_id}")
    if resp:
        name = resp.json().get('name')
        return name
    return None


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Syntax: python3 0-gather_data_from_an_API.py <EMPLOYEE_ID>")
        exit(1)

    employee_id = sys.argv[1]
    name = get_employee_name(employee_id)
    tasks = get_tasks(employee_id)

    completed_tasks = list()
    for task in tasks:
        if not task.get("completed"):
            continue
        completed_tasks.append(task.get('title'))

    print("Employee {name} is done with tasks({ct}/{tt}):".format(
        name=name, ct=len(completed_tasks), tt=len(tasks)))

    for title in completed_tasks:
        print("\t {t}".format(t=title))
