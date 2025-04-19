# Python gRPC Examples

## Setup
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install grpcio-tools
```

## Usage
```bash
bash genproto.sh

# server
python bserver.py

# client
python bclient.py
```