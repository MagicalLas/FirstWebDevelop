FROM python:3.7

MAINTAINER Las-Wonho haho6629@gmail.com

COPY . .

RUN apt-get update && apt-get install nginx

RUN pip install -r requirements.txt