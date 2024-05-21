#!/usr/bin/python3
"""a script that returns information about the progress of
an employee's to-do list using REST API
"""
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com"
    user = requests.get(api+'/users/'+user_id)

    employee_name = user.json().get('name')

    todos = requests.get(api+'/todos')
    total_tasks = 0
    completed = 0

    for task in todos.json():
        if task.get('user_id') == int(user_id):
            total_tasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, completed, total_tasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('user_id') == int(user_id) and task.get('completed')]))
