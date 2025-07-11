FROM python:3.9-slim

WORKDIR /app

COPY result_app.py .

RUN pip install flask redis

EXPOSE 80

CMD ["python", "result_app.py"]

