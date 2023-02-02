# Install
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r packages.txt
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

# Run server
```sh
cd backend
python manage.py runserver
```

# API
## Register
```sh
http://localhost:8000/api/users/register/
Method: POST
Body:(json format)
{
    "email": "input email",
    "password": "input password",
}
```
## Login
```sh
http://localhost:8000/api/users/login/
Method: POST
Body:(json format)
{
    "email": "input email",
    "password": "input password",
}
```
## Add task
```sh
http://localhost:8000/api/todo/
Method: POST
Header: Authorization: Bearer {token}
Body:(json format)
{
    "title": "input title",
    "description": "input description",
}
```
## Get all task
```sh
http://localhost:8000/api/todo/
Method: GET
```
## Get task with id
```sh
http://localhost:8000/api/todo/{id}/
Method: GET
Header: Authorization: Bearer {token}
```
## Update task with id
```sh
http://localhost:8000/api/todo/{id}/
Method: PUT
Header: Authorization: Bearer {token}
Body:(json format)
{
    "title": "input title",
    "description": "input description",
}
```
## Delete task with id
```sh
http://localhost:8000/api/todo/{id}/
Method: DELETE
Header: Authorization: Bearer {token}
```