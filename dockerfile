FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Set python path
ENV PYTHONPATH=/app

# Create artifacts directory
RUN mkdir -p data artifacts/release

# Default command
CMD ["python", "src/main.py"]