FROM python:3.10.3-alpine

COPY . ./hello
WORKDIR ./hello

CMD [ "python3", "sample.py" ]