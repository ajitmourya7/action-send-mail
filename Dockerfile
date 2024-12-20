FROM python:3.10.13-slim

# Set the working directory
WORKDIR /app

# Copy files into the container
COPY send_email.py /app/

# Install SendGrid Python library
RUN pip install --no-cache-dir sendgrid

# Set the entry point to the Python script
ENTRYPOINT ["python", "/app/send_email.py"]
