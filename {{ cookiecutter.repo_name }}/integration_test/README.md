# Integration test

Relative to repo top level

## Start service for test.
```bash
make docker
>>> docker_id
```
Then, either
```bash
docker run --cpus=8 --memory=2gb -it --rm -p 5000:{{ cookiecutter.gunicorn_port }} --name={{ cookiecutter.repo_name}}-e2e <docker_id>
docker run --gpus=1 --cpus=8 --memory=2gb -it --rm -p 5000:{{ cookiecutter.gunicorn_port }} --name={{ cookiecutter.repo_name }}-e2e <docker_id>
```

## Run test.
In the other terminal. Run below to start the test.

```python
SVC_ADDRESS=http://127.0.0.1:5000 CLIENT_TIMEOUT=60 pytest -rA integration_test/
```
