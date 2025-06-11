FROM python:3.14.0b2-alpine3.22

WORKDIR app

COPY movies-api/requirments.txt .

RUN pip install -r requirments.txt

COPY movies-api/movies.py .

EXPOSE 80

CMD ["pyton3", "movies.py"]