FROM apache/superset:latest
USER root

COPY psycopg2_binary-*.whl /tmp/
RUN pip install /tmp/psycopg2_binary-*.whl

USER superset