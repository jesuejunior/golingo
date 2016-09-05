FROM jesuejunior/python:3

COPY . /app

WORKDIR /app

RUN pip install -r requirements.pip \
	&& python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--log-file", "/var/log/rocketlang.error.log",  "-w", "2", "rocketlang.wsgi:application"]
