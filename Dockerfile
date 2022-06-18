FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

ENV EASYMODE_CONFIG /config

COPY ./app /app
RUN pip install -r /app/requirements.txt
