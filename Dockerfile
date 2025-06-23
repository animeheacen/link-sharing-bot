FROM python:3.8-slim-buster

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
