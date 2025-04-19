FROM python:3.12-slim

WORKDIR /app
RUN pip install -U grpcio grpcio-tools

COPY rpc/ rpc/
COPY aserver.py .

CMD ["python", "-u", "aserver.py"]