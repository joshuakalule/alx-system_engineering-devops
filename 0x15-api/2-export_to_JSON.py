#!/usr/bin/python3
"""
Gather data from an API
Queries 'https://jsonplaceholder.typicode.com/' for a given employee ID
Return employee information
"""
import json
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'


def get_tasks(employee_id):
    """Get the tasks of the employee."""
    resp = requests.get(f"{API_URL}/users/{employee_id}/todos")
    if resp:
        return resp.json()
    return {}


def employee_get(employee_id, key):
    """Get the key of the employee."""
    resp = requests.get(f"{API_URL}/users/{employee_id}")
    if resp:
        name = resp.json().get(key, None)
        return name
    return None


def export_json(employee_id, username, tasks):
    """Export to json."""
    return_dict = {employee_id: [], }
    for task in tasks:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        return_dict[employee_id].append(task_dict)

    file_path = f"{employee_id}.json"
    with open(file_path, 'w') as jsonfile:
        json.dump(return_dict, jsonfile)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Syntax: python3 0-gather_data_from_an_API.py <EMPLOYEE_ID>")
        exit(1)

    employee_id = sys.argv[1]
    username = employee_get(employee_id, "username")
    tasks = get_tasks(employee_id)

    export_json(employee_id, username, tasks)
