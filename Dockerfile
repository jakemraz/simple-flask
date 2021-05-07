FROM python:3.7.7-buster

ENV PYTHONUNBUFFERED=TRUE

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
COPY supervisord.conf supervisord.conf

COPY entrypoint.sh entrypoint.sh
RUN chmod 755 entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
