FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask redis
EXPOSE 80
CMD ["python", "app.py"]

