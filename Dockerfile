FROM python:3.9

WORKDIR usr/src/shipping_rest


COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/shipping_rest
