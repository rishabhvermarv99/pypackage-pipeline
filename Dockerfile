
FROM python:3.8-slim

WORKDIR /app

RUN pip install sigmoidpythonlib

EXPOSE 80

CMD ["python", "-m", "sigmoidpythonlib"]
