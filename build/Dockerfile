FROM python:3.9 as builder

WORKDIR /app
ADD src .

RUN \
    apt-get update && \
    apt-get install espeak-ng espeak-ng-espeak portaudio19-dev -y && \
    apt-get autoclean -y && \
    apt-get autoremove -y
RUN \
    pip install -r requirements.txt
RUN \
    mkdir /output

ENV AUDIO_ENABLED=false

EXPOSE 8124

VOLUME /output

CMD ["python", "-u", "./glados.py", "serve","--port", "8124", "--host", "0.0.0.0"]

