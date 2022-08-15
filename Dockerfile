#FROM python:3.8.5
#
#ADD ./requirements.txt /app/requirements.txt
#
#RUN set -ex \
#    && python -m venv /env \
#    && /env/bin/pip install --upgrade pip \
#    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
#    && runDeps="$(scanelf --needed --nobanner --recursive /env \
#        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
#        | sort -u \
#        | xargs -r apk info --installed \
#        | sort -u)"
#
#
#ADD painter /app
#WORKDIR /app
#
#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH
#
#ENV DJANGO_SETTINGS_MODULE 'config.settings'
#ENV VERSION 1
#ENV SERVICE_ENV 'dev'
#
#EXPOSE 8001
#
#CMD ["gunicorn", "--bind", ":8005", "--workers", "3", "--keep-alive", "600", "--timeout", "600" ,"config.wsgi:application"]

