# Use the official Python image as the base image
# docker image build -t mail-script -f Dockerfile .
## $ docker tag mail-script:latest ramalin/mailscript:v1.1.2
## $ docker push ramalin/mailscript:v1.1.2

FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the required libraries
RUN pip install requests
RUN pip install python-dotenv


# Copy your Python script to the container
COPY login.py /app

# Run the Python script when the container starts
CMD ["python", "/app/login.py"]

