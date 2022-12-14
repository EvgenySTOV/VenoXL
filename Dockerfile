FROM python:3.6-alpine

EXPOSE 5000

WORKDIR /venoxapp

RUN python3 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Bank .

ENTRYPOINT python3 app.py
