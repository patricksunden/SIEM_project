# Dockerfile

FROM docker.elastic.co/logstash/logstash:8.9.0

USER root

RUN logstash-plugin install logstash-output-opensearch
RUN logstash-plugin install logstash-input-opensearch

USER logstash

COPY ./logstash.conf /usr/share/logstash/pipeline/logstash.conf
