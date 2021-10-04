# set the base image
FROM python:3.8-slim

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /usr/src/app/logs/
CMD python ./app.py