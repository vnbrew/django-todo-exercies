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
http://localhost:8000/users/register/
Method: POST
Body:(json format)
{
    "email": "input email",
    "password": "input password",
}
```
## Login
```sh
http://localhost:8000/users/login/
Method: POST
Body:(json format)
{
    "email": "input email",
    "password": "input password",
}
```