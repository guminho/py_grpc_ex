FROM python:3.10-slim

WORKDIR /app

RUN pip install grpcio protobuf
COPY . .

CMD ["python", "srv.py"]