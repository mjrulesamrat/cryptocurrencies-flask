FROM ubuntu:latest
MAINTAINER Aditya Krishnakumar "aditya.kkumar97@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements/base.txt
# ENTRYPOINT ["python"]
# CMD ["app.py"]
ENV FLASK_APP /app/cryptocurrencies.py
CMD flask run --host=0.0.0.0