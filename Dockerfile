FROM tiangolo/uvicorn-gunicorn:python3.7

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host=mirrors.aliyun.com
