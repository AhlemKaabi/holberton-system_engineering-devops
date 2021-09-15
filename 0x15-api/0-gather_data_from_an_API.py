#!/usr/bin/python3
"""
Python script that, uses REST API (https://jsonplaceholder.typicode.com/todos)
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys #argv = id
# sys.stdout.write(<the employee TODO list progress>)
#output:
#Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

    # EMPLOYEE_NAME: name of the employee
    # NUMBER_OF_DONE_TASKS: number of completed tasks
    # TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
#Second and N next lines display the title of completed tasks:
#TASK_TITLE (with 1 tabulation and 1 space before the
if __name__ == "__main__":

    number_completed_todos = 0
    number_of_todos = 0
    completed_tasks = []

    user_url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    user_infos = requests.get(user_url).json()

    user_name = user_infos.get("name")

    user_todos_url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1] + '/todos/'
    user_todos = requests.get(user_todos_url).json()

    for user_todo in user_todos:
        number_of_todos += 1
        if (user_todo.get("completed") == True):
            number_completed_todos += 1
            completed_tasks.append(user_todo.get("title"))


    print("Employee {} is done with taks({}/{}):".format(
        user_name,
        number_completed_todos,
        number_of_todos
        ))
    for task in completed_tasks:
        print("\t {}".format(task))
