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
CSV_FILE_PATH = 'todo_all_employees.json'


def get_tasks(employee_id):
    """Get the tasks of the employee."""
    resp = requests.get(f"{API_URL}/users/{employee_id}/todos")
    if resp:
        return resp.json()
    return {}


def compile_list(employee_id, username, tasks):
    """Generate task list for employee."""
    task_list = list()
    for task in tasks:
        task_dict = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        task_list.append(task_dict)

    return task_list


def cycle_employees():
    """Loop through all employees and return dictionary."""
    resp = requests.get(f"{API_URL}/users")
    if not resp:
        exit()
    employees = resp.json()

    dict_obj = dict()
    for employee in employees:
        employee_id = employee.get('id')
        username = employee.get('username')
        tasks = get_tasks(employee_id)

        dict_obj[employee_id] = compile_list(employee_id, username, tasks)
    return dict_obj


def export_json(dict_obj):
    """Export to json."""
    with open(CSV_FILE_PATH, 'w') as jsonfile:
        json.dump(dict_obj, jsonfile)


if __name__ == "__main__":

    employee_dict = cycle_employees()
    export_json(employee_dict)
