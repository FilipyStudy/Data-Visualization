FROM python:3.12

WORKDIR /app

COPY /requirements.txt .
COPY elt_script.py .

RUN apt-get update -y
RUN apt-get install -y postgresql-client python3-pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "elt_script.py"]