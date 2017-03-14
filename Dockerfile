FROM python:3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        python-dev \
        python-psycopg2 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .

ENV DEBUG False
ENV PROD True

EXPOSE 8000

WORKDIR /usr/src/app/

CMD ["gunicorn", "slackbot.wsgi", "-b", "0.0.0.0:8000"]