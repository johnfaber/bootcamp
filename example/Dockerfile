FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py app.py

EXPOSE 5000

CMD [ "python3", "app.py"]
