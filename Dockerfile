FROM python:3.9.1

WORKDIR /app

COPY ./fib.py .

CMD ["python", "fib.py"]
