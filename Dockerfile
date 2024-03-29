FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt


COPY ./src /code/

EXPOSE 8002

RUN chmod +x /code/start.sh

ENTRYPOINT ["sh","/code/start.sh"]