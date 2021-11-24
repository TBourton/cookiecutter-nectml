FROM {{ cookiecutter.docker_image }}
LABEL maintainer="{{ cookiecutter.author_initials }} <{{ cookiecutter.author_email }}>"

RUN useradd python -u 10001 --create-home --user-group
WORKDIR /app

ENV PIP_NO_CACHE_DIR 1
ENV PIP_DISABLE_VERSION_CHECK 1
ENV PIP_INDEX_URL https://nexus.int.svc.nect.com/repository/pypi-group/simple


COPY --chown=python ./deps/result ./deps/result
RUN cd deps/result && pip install {{ cookiecutter.namespace_name }}.result* && cd ../..

COPY --chown=python ./deps/core ./deps/core
RUN cd deps/core && pip install {{ cookiecutter.namespace_name }}.core* && cd ../..

COPY --chown=python requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY --chown=python config.yaml .
ENV {{ cookiecutter.namespace_name.upper() }}_CONF ./config.yaml

COPY --chown=python logging.yaml .
ENV LOGGING_CONF logging.yaml

COPY --chown=python gunicorn.conf.py .
ENV GUNICORN_CONF ./gunicorn.conf.py
ENV GUNICORN_CMD_ARGS "--config $GUNICORN_CONF"

COPY --chown=python {{ cookiecutter.namespace_name }} ./{{ cookiecutter.namespace_name }}

ENV METRICS_PORT 9200

USER python

CMD [ "gunicorn", "{{ cookiecutter.namespace_name }}.service.jlgeh:app" ]
