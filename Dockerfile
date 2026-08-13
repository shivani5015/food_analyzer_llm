FROM python:3.11-slim

WORKDIR /app

# Copy requirements file first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

EXPOSE 8000

# Command to run application inside Docker container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]