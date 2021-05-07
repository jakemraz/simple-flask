# simple-flask
simple flask application with port control

# How to use
```shell
$ python3 -m pip install -r requirements.txt
$ gunicorn app:app -b 0.0.0.0:80 --threads 2
```

# Dockerize
```shell
# it will make simple_flask:latest image
$ docker build -t simple_flask .
```
# Run command
After dockerize, execute the command below
```shell
$ docker run -it -p <local>:80 simple_flask

# for example
$ docker run -it -p 80:80 simple_flask
```
