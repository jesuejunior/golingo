FROM python:3.4.3

RUN apt-get -y update \
	&& apt-get -y install python-pip \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY . /golingo

WORKDIR /golingo

RUN pip install -r requirements.pip

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "golingo.wsgi:application"]