
FROM mcr.microsoft.com/playwright/python:v1.60.0-jammy

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir playwright

CMD ["python", "app.py"]
