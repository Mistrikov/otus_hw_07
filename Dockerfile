from python:3.11

RUN apt-get update
RUN pip3 install --upgrade pip

COPY ./ ./
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn