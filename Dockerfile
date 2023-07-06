FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
