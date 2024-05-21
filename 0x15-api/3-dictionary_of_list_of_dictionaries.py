#!/usr/bin/python3
"""a script to export extracted data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()
    todoObj = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDic = {'username': user.get('username'),
                           'task': task.get('title'),
                           'completed': task.get('completed')}
                taskList.append(taskDic)
        todoObj[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as jsonFile:
        json.dump(todoObj, jsonFile)
