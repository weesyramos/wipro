FROM python:3.6

WORKDIR /backend

COPY . .

RUN pip install -r requirements/local.txt

CMD ["python", "manage.py", "runserver"]
