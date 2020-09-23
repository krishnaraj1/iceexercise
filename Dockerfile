FROM python:3.7.9-alpine3.12
RUN pip install pika
COPY ./send.py /send.py
CMD ["/usr/local/bin/python", "/send.py"]
