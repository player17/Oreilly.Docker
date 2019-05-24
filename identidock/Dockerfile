FROM python:3.7

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==0.10.1 uWSGI==2.0.18
WORKDIR /app
COPY app /app
COPY tmp /app

EXPOSE 9090 9191
USER uwsgi

CMD ["./cdm.sh"]
