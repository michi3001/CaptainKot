FROM python:3.11-slim

WORKDIR /app/

COPY ./PythonClient/requirements.txt .
RUN pip install -r requirements.txt

COPY ./KotlinCompiler/schemas/ ./

COPY ./PythonClient/client.py ./

EXPOSE 80

CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "80", "--reload"]