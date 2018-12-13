FROM python:3

WORKDIR .
ADD . /bot

CMD app.py