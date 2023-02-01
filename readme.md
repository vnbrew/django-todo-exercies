# Install
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r packages.txt
```

# API
## Register
```sh
http://localhost:8000/users/register/
Method: POST
Body:(json format)
{
    "username": "input username",
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
    "username": "input username",
    "password": "input password",
}
```