FROM python:3.10
RUN python -m pip install --upgrade pip

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt

COPY people/ ./people/
COPY people_service/ ./people_service/
COPY manage.py manage.py
COPY sample_data.json sample_data.json

RUN python manage.py migrate
RUN python manage.py loaddata sample_data.json

EXPOSE 8000/tcp

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]