FROM python:3.11.7-alpine3.18

RUN apk add --no-cache bash

COPY . /app
WORKDIR /app
EXPOSE 8000

RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]