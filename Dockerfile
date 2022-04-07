FROM python:3.10

WORKDIR /APP

COPY . /APP/

RUN pip install -r ./requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver" , "0.0.0.0:8000"]
