FROM python:3.7.12-alpine

COPY src/main.py main.py

ENTRYPOINT [ "python", "main.py" ]
