FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "--app", "app", "run", "--host", "0.0.0.0" ]
