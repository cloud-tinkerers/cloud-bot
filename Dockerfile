FROM python:3.11.9-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY /src .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "__main__.py"]