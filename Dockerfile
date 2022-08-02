FROM python:3.10

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

CMD python /code/manage.py makemigrations && python /code/manage.py migrate && python /code/manage.py loaddata initial_data.json && python /code/manage.py runserver 0.0.0.0:8000