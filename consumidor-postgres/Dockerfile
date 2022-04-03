FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-venv

WORKDIR /app
COPY . /app

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

CMD python3 app.py
