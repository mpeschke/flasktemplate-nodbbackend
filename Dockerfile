FROM ubuntu:jammy

COPY system-ubuntu20-dependencies.sh /opt/api/system-ubuntu20-dependencies.sh
RUN chmod +x /opt/api/system-ubuntu20-dependencies.sh
RUN /opt/api/system-ubuntu20-dependencies.sh

COPY requirements.txt /opt/api/requirements.txt
RUN pip3 install -r /opt/api/requirements.txt

COPY wsgi.py /opt/wsgi.py
COPY api /opt/api

WORKDIR /opt

ENV CONFIGENV=api.config.TestingConfig
ENV PYTHONDONTWRITEBYTECODE=1
ENV WEBSERVHOST=0.0.0.0
ENV WEBSERVPORT=8080
ENV WORKERS=4

ARG USERNAME=api
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

USER $USERNAME

EXPOSE $WEBSERVPORT

ENTRYPOINT "gunicorn" \
"-w" \
"$WORKERS" \
"-b" \
"$WEBSERVHOST:$WEBSERVPORT" \
"--access-logfile" \
"-" \
"wsgi:APP"