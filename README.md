# IGS Employee Manager
This is a project created as part of the IGS challenge for the Django framework. The goal of this project is to create a web application for managing employee information.

# Installation

Clone the GitHub repository to your computer 

# Usage

Open your browser and access the address http://localhost:8000/

To access the administration area, access the address http://localhost:8000/admin/ and login with the administrator credentials (username: admin and password: admin).

To add, edit, or delete employee information, access the application's homepage and use the provided forms.

To access the public site containing a simple table with the data registered in the app, access the address http://localhost:8000/public/.

# API Endpoints

This is a RESTful API created as part of the IGS Employee Manager app. The API allows developers to access and manipulate employee information.

There are two main routes of the API: /employee/ and /department/. Each route supports GET, POST, and DELETE methods.

The /employee/ route is used to list, add, and delete employee data. The GET method returns all employees currently stored in the database, the POST method allows adding a new employee, and the DELETE method removes an employee based on their name.

The /department/ route is used to list, add, and delete department data. The GET method returns all departments currently stored in the database, the POST method allows adding a new department, and the DELETE method removes a department based on its name.

# API Examples

#### Get all employees

```python
url = 'http://localhost:8000/employee/'

response = requests.get(url)

print(response.json())
```
This will return a JSON object containing all employees in the database.

#### Add a new employee

```python
url = 'http://localhost:8000/employee/'

data = json.dumps({'name': 'Joao', 'email': 'name@example.com', 'department': 'Sales'})

response = requests.post(url, data=data)

print(response.json())
```

This will return a successful message.

#### Delete an employee

```python
url = 'http://localhost:8000/employee/'

params = {'name': 'Joao'}

response = requests.delete(url, params=params)

print(response.json())
```

This will return a successful message.

#### Get all departments

```python
url = 'http://localhost:8000/department/'

response = requests.get(url)

print(response.json())
```
This will return a JSON object containing all departments in the database.

#### Add a new department
```python
url = 'http://localhost:8000/department/'

data = {'name': 'IT'}

response = requests.post(url, data=data)

print(response.json())
```
This will return a successful message.

#### Delete a department
```python
url = 'http://localhost:8000/department/'

params = {'name': 'IT'}

response = requests.delete(url, params=params)

print(response.json())
```
This will return a successful message.
