FROM python:3.5.9-alpine

ARG WORK_DIR=/usr/src/app

RUN mkdir -p $WORK_DIR
WORKDIR $WORK_DIR
COPY sleep.py ./
CMD ["python", "sleep.py"]
