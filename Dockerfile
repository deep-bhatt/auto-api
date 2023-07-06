FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["bash", "run.sh"]
