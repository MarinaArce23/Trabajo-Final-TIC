FROM python:3.10-slim

WORKDIR /app

COPY ../requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ../app.py ./app.py
COPY ../templates ./templates

EXPOSE 5000

CMD ["python", "app.py"]

