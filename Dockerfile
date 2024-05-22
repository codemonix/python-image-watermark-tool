FROM python:3.10-slim

ENV DISPLAY=:0

RUN apt-get update && \
    apt-get install -y python3-tk && \
    apt-get install -y x11-apps && \
    apt-get clean

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD [ "python", "app.py" ]