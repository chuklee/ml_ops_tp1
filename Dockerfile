# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies with verbose output
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -v

# Copy the application code and model_utils.py
COPY app.py ./
COPY model_utils.py ./

# Expose the port the app runs on
EXPOSE 4872

# Command to run the application
CMD ["python", "app.py"]