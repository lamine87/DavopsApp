FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install numpy

CMD [ "python", "app.py" ]