FROM python:buster

RUN pip install paho-mqtt & pip install requests

WORKDIR /var/levande/

COPY ./src/python /var/levande/

ENV PYTHONUNBUFFERED 1

CMD [ "python", "./main.py" ]