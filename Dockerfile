FROM python:3.9.1

WORKDIR /app

COPY ./labfirst.py .

CMD ["python", "labfirst.py"]
