FROM python:3

WORKDIR /app


RUN pip3 install Flask flask_restful requests

COPY ./src ./src

ENV PORT = 8081

EXPOSE 8081

CMD [ "python", "./src/index.py"]

