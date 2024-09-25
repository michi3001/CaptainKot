FROM python:3.11-slim

WORKDIR /app/

RUN apt-get update && \
    apt-get install -y capnproto autoconf automake libtool curl make g++ unzip && \
    apt-get clean

RUN pip install pycapnp

COPY ./PythonClient/requirements.txt .
RUN pip install -r requirements.txt

COPY ./KotlinCompiler/schemas/ ./

COPY ./PythonClient/client.py ./

CMD ["python", "client.py"]