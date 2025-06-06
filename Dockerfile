FROM apache/superset:latest
USER root

# Копируем все .whl файлы из папки whl
COPY whl/*.whl /tmp/wheels/

# Устанавливаем все пакеты из .whl файлов
RUN pip install /tmp/wheels/*.whl

USER superset