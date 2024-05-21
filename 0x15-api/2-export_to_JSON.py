#!/usr/bin/python3
"""a script to export extracted data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDic = {"task": task.get('title'),
                       "completed": task.get('completed'),
                       "username": user.json().get('username')}
            taskList.append(taskDic)
    todoUser[userId] = taskList

    newFile = userId + '.json'
    with open(newFile, mode='w') as jsonFile:
        json.dump(todoUser, jsonFile)
