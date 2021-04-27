# simple-flask
simple flask application with port control

# How to use
```python
$ python3 run.py <port> <signiture>
```

# Example
```python
$ $ python3 run.py 80 1
```
It will run Flask app on 80 port.
You can get the resulf of 1 if you access this port.
```
$ curl 127.0.0.1:80
hello flask 1
```

# For AWS EC2 UserData
```bash
#!/bin/bash
yum install -y git
yum install -y python3
git clone https://github.com/jakemraz/simple-flask.git
python3 -m pip install -r simple-flask/requirements.txt
python3 simple-flask/run.py <port> <signature>
```