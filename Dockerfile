FROM alpine:3.3

RUN apk add --no-cache python3 python3-dev libpq gcc  linux-headers musl-dev postgresql-dev && \
    apk add --no-cache --virtual=build-dependencies wget ca-certificates && \
    wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \
    apk del build-dependencies

COPY . /golingo

WORKDIR /golingo

RUN pip install -r requirements.pip \
	&& python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "--log-file", "/var/log/golingo.error.log",  "-w", "2", "golingo.wsgi:application"]
