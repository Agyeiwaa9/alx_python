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

def export_all_to_json():
    filename = 'todo_all_employees.json'

    all_data = {}

    for employee_id in range(1, 11):  # Assuming there are 10 employees, adjust as needed
        try:
            employee_data = get_employee_data(employee_id)
            employee_name = employee_data['name']
            todo_list = get_todo_list(employee_id)

            all_data[employee_id] = [
                {"username": employee_name, "task": task['title'], "completed": task['completed']}
                for task in todo_list
            ]

        except requests.RequestException as e:
            print(f"Error fetching data for employee {employee_id}: {e}")

    with open(filename, 'w') as jsonfile:
        json.dump(all_data, jsonfile, indent=2)

    print(f"Data exported to {filename}")

def main():
    export_all_to_json()

if __name__ == "__main__":
    main()
