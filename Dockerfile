FROM python:3.8-alpine

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY ./src /app
WORKDIR /app
CMD ["python", "app.py"]
# Expose the port the app runs on
EXPOSE 5000
# Set environment variables
ENV FLASK_APP=app.py