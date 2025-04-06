# Stage 1: Build stage
FROM python:3.10-slim-bullseye as builder

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies globally
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.10-slim-bullseye

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy installed Python packages from builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source code
COPY . .

# Expose application port
EXPOSE 5000

# Run the application
CMD ["python3", "server.py"]
