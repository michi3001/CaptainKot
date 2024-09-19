FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y capnproto autoconf automake libtool curl make g++ unzip && \
    apt-get clean

RUN pip install pycapnp

WORKDIR /usr/src/app

COPY example.capnp ./
COPY server.py ./
COPY client.py ./