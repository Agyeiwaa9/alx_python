import requests
import sys

def get_employee_data(employee_id):
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()
    return employee_data

def get_todo_list(employee_id):
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(todo_url)
    todo_list = response.json()
    return todo_list

def display_progress(employee_name, done_tasks, total_tasks, completed_tasks):
    print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_data = get_employee_data(employee_id)
        employee_name = employee_data['name']

        todo_list = get_todo_list(employee_id)
        total_tasks = len(todo_list)
        done_tasks = sum(1 for task in todo_list if task['completed'])
        completed_tasks = [task for task in todo_list if task['completed']]

        display_progress(employee_name, done_tasks, total_tasks, completed_tasks)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

