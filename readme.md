# Python gRPC Examples

## Setup
```bash
python3 -m venv venv
. venv/bin/activate
pip install grpcio-tools
```

## Usage
```bash
cd hello
bash genproto.sh

# server
python srv.py

# client
python cli.py
```