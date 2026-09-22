FROM python:3.13-slim

WORKDIR /app

COPY test.py .

CMD ["python3", "test.py"]
