# Backend Coding Challenge

### How to
build the image:
```
docker build . -t idoven
```

run the tests:
```
docker run -p 8000:8000 idoven python -m pytest tests
```

run the api:
```
docker run -p 8000:8000 idoven
```

## Endpoints

Try it
* http://localhost:8000/docs

Read Ecgs
* [GET] /ecgs

Create Ecgs
* [POST] /ecgs

Create User
* /users/create

Login
* /users/login

### consideations

* these are the example users:

admin
```
admin
admin
```

normal user
```
test
test
```
* persistence.py emulates a db using program memory
* authentication is jwt based (Bearer Token)

### TODO
* e2e tests
* better unit testing
* implement a real db driver (mongodb for example, even redis)
