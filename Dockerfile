FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && rm requirements.txt
