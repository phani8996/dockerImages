FROM alpine:latest
#FROM python:3.5.9-alpine
ARG AUTH_TOKEN
ARG BIND_TLS=false
ARG REGION=in
ARG WORK_DIR=/usr/app/src

RUN mkdir -p $WORK_DIR
WORKDIR $WORK_DIR
#RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
COPY ngrok-stable-linux-arm.zip ./ 
RUN unzip ngrok-stable-linux-arm.zip
RUN ./ngrok authtoken $AUTH_TOKEN 
RUN rm ./ngrok-stable-linux-arm.zip
RUN echo "web_addr: 0.0.0.0:4040" >> ~/.ngrok2/ngrok.yml
RUN cat ~/.ngrok2/ngrok.yml
CMD ["./ngrok", "http", "traefik:80", "--bind-tls", "false", "--region", "in", "--log", "stdout"]
