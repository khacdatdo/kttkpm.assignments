FROM python:3.10-rc-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
