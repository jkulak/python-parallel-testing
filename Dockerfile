# Stage 1: Build
FROM python:3.12 as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Run
FROM python:3.12.0-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY src/main.py .

# Make sure scripts in .local are usable:
ENV PATH=/root/.local:$PATH

CMD ["python", "./main.py"]
