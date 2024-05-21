#!/usr/bin/python3
"""a script that returns information about the progress of
an employee's to-do list using REST API
"""
import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com"
    user = requests.get(api+'/users/'+userId)

    employeeName = user.json().get('name')

    todos = requests.get(api+'/todos')
    allTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            allTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employeeName, completed, allTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
