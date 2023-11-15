# Stage 1: Build
FROM python:3.12 as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Run
FROM python:3.12.0-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY src/main.py .

CMD ["python", "./main.py"]
