FROM python:3.10-slim-buster

COPY requirements.txt .
COPY elt_script.py .

RUN apt-get update && apt-get install -y postgresql-client python3-pip
RUN pip install --upgrade pip \ 
    && pip install -r requirements.txt

CMD ["python", "elt_script.py"]