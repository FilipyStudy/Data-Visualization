FROM python:latest

COPY . .
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip install -r requirements.txt

CMD [ "python", "etl_script.py" ]