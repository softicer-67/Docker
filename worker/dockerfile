FROM python:3.10

WORKDIR ./app

RUN pip install redis

COPY . /app/

CMD python worker.py
