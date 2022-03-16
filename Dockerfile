FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY . /taste_dive
WORKDIR /taste_dive

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "-u", "wsgi.py"]