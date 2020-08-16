# Technical Test Backend, IT CROWD

## Cinemapi REST API
  

- [Technical Test Backend, IT CROWD](#technical-test-backend-it-crowd)
  - [Cinemapi REST API](#cinemapi-rest-api)
    - [Requirements for running the project](#requirements-for-running-the-project)
    - [Running the project in local and debug mode](#running-the-project-in-local-and-debug-mode)
    - [Project deployed in AWS](#project-deployed-in-aws)
    - [Enpoints documentation](#enpoints-documentation)
    - [Libraries and frameworks used.](#libraries-and-frameworks-used)

### Requirements for running the project

  
- Docker

- Docker Compose
  

### Running the project in local and debug mode

After clone the repo, you need to build the docker image and run it:

  

`docker-compose up`

  

The project runs on `http://localhost:8000/`


### Project deployed in AWS

[http://ec2-52-90-243-117.compute-1.amazonaws.com](http://ec2-52-90-243-117.compute-1.amazonaws.com/) shows this code deployed in a EC2 instance using a RDS instance with postgres engine like Database project.

You can try all available methods using an interface to browse items and also to create/edit/delete items. The current credentials are:
```bash
Username: django
Password: Mnzx9874
```

### Enpoints documentation

The available endpoints and supported methods documented are in this [redoc url](http://ec2-52-90-243-117.compute-1.amazonaws.com/redoc/)

After you login, here you can **Try it out** all movies and persons methods: GET, POST, PUT, PATCH and DELETE

### Libraries and frameworks used.


| Type | Name  | Reason | 
|--|--|--|
| Framework | Django | This is fast, simple, secure, well-established and supportive community accessed through numerous forums, channels, and dedicated websites.  | 
| Framework | Django Rest Framework | DRF makes developing API’s simple and you can use it just for developing API for some web service in Backend, separated from Frontend |
| Library | psycopg2 | Psycopg2 is the most popular python driver for PostgreSQL. Actively maintained and support the major version of python i.e. Python 3 and Python 2. It was designed for heavily multi-threaded applications. |
| Library | drf-yasg | Using drf-yasg, you can create APIs in a more organized and user-friendly way and basicaly because support: nested serializers and schemas nad response schemas and descriptions. |
| Tool | Docker compose | Like a tool for defining and running multi-container Docker applications. Compose works in all environments: production, staging, development, testing, as well as CI workflows. It allows make deployement simple. |
