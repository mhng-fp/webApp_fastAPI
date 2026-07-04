FROM python:3.14

WORKDIR /code

# Copies requirements from your root folder
COPY requirements.txt /code/requirements.txt

# Installs your Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# FIX: Preserves the "app" folder structure inside /code
COPY app /code/app

# Starts your FastAPI application flawlessly
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
