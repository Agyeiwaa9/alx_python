import requests
import json
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

def export_to_json(employee_id, employee_name, todo_list):
    filename = f'{employee_id}.json'

    data = {
        "USER_ID": [
            {"task": task['title'], "completed": task['completed'], "username": employee_name}
            for task in todo_list
        ]
    }

    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

    print(f"Data exported to {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        employee_data = get_employee_data(employee_id)
        employee_name = employee_data['name']

        todo_list = get_todo_list(employee_id)

        display_progress(employee_name, todo_list)

        export_to_json(employee_id, employee_name, todo_list)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
