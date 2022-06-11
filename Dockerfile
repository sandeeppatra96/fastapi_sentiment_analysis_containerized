
# Get the Fast API image with Python version 3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Create the directory for the container

COPY requirements.txt ./requirements.txt
COPY main.py ./main.py

# Install the dependencies
RUN pip install -r requirements.txt


# Run by specifying the host and port
CMD ["uvicorn", "main:appi", "--host", "0.0.0.0", "--port", "80"]
