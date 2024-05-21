#!/usr/bin/python3
"""a script to export extracted data in CSV format"""

if __name__ == "__main__":
    import requests
    import csv
    from sys import argv

    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(argv[1]))
    username = r.json().get('username')

    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                     format(argv[1]))
    data = r.json()

    with open('{}.csv'.format(argv[1]), mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in data:
            csv_writer.writerow([argv[1], username, task.get('completed'),
                                 task.get('title')])
