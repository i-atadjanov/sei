# 1. Python language
FROM python:3.10-slim

RUN python -m pip install --upgrade pip
# 2. setting the working directory inside the container
WORKDIR /app

# 3. Copy dependencies list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest
COPY . .

# 5. Running commmand
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]