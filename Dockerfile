FROM nginx:1.25.5-alpine-slim

RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN apk add py3-flask

WORKDIR /app

COPY . .
EXPOSE 80
CMD ["python3","-m","flask","--app","app","run","--host=0.0.0.0","--port=80"]