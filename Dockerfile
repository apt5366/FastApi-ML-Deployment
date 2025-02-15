# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /code

# Upgrade pip first to avoid dependency issues
RUN pip install --upgrade pip 

# Copy requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install  --no-cache-dir -r /code/requirements.txt

# Copy application files
COPY ./app /code/app

# Expose FastAPI's default port
EXPOSE 8000


# Run FastAPI application
CMD ["python", "-m", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]


