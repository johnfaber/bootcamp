FROM python:3.9-alpine

WORKDIR /app

COPY reqs.txt reqs.txt

ENV ENV=lab_02

RUN pip3 install --no-cache-dir -r reqs.txt

COPY lab_02.py app.py

EXPOSE 5000

CMD [ "python3", "app.py"]
