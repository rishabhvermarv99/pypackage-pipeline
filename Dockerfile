FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install sigmoidpythonlib

ARG GIT_SHA

EXPOSE 80

CMD ["python", "-m", "sigmoidpythonlib"]
