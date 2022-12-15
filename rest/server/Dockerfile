FROM python:3.10-slim

#FastAPI libraries
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

WORKDIR /data

