#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        url_info = "https://jsonplaceholder.typicode.com/users/{}/".format(
            user_id)
        response = requests.get(url_info).json()
        username = response.get("username")
        url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user_id)
        user_todos = requests.get(url_todo).json()
        file_name = "{}.json".format(user_id)
        all_data = {}
        data_list = []
        for todo in user_todos:
            data = {}
            data['task'] = todo.get('title')
            data['completed'] = todo.get('completed')
            data['username'] = username
            data_list.append(data)
        data[user_id] = data_list
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except ValueError:
        exit()
