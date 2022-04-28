FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential daphne

RUN mkdir /core

WORKDIR /core

COPY requirements.txt .
COPY entrypoint.sh .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=100 future
RUN chmod +x entrypoint.sh

COPY . .


ENTRYPOINT ["/core/entrypoint.sh"]