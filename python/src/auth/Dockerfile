FROM python:3.10-slim-bullseye

# Configure apt for better network handling and install dependencies
RUN echo 'Acquire::Retries "3";' > /etc/apt/apt.conf.d/80-retries && \
    echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 && \
    echo 'Acquire::http::Timeout "10";' > /etc/apt/apt.conf.d/80-timeouts && \
    echo 'Acquire::https::Timeout "10";' >> /etc/apt/apt.conf.d/80-timeouts && \
    sed -i 's|http://ftp.debian.org|http://deb.debian.org|' /etc/apt/sources.list && \
    apt-get clean && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    gnupg \
    ca-certificates \
    build-essential \
    default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*  # Cleanup unnecessary package lists

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app

EXPOSE 5000
CMD ["python3", "server.py"]
