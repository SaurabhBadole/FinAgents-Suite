# Use the official lightweight Python image.
FROM python:3.12.4-slim

# Set the working directory
WORKDIR /app


# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the Streamlit application
CMD ["streamlit", "run", "FinAgents_Suite.py"]
