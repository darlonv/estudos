FROM python:3.10-slim

#OpenCv dependencies
RUN apt update
RUN apt -y install ffmpeg libsm6 libxext6

#OpenCv libraries
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

WORKDIR /data

