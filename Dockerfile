# 1) Use an official lightweight Python image
FROM python:3.13-slim

# 2) Set the working directory inside the container
WORKDIR /app

# 3) Copy and install dependencies first (layer caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copy the rest of your project code
COPY . .

# 5) Expose FastAPI port
EXPOSE 8000

# 6) Start the FastAPI server when the container runs
# "api:app" → api.py file and the FastAPI "app" instance inside it
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
