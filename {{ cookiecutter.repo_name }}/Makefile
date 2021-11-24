PYTHON_BIN ?= python3

deps:
	pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements-dev.txt
	cd result && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install ${PIP_ARGS} . && cd ..
	cd core  && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install ${PIP_ARGS} . && cd ..
	cd client && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install ${PIP_ARGS} . && cd ..
	cd service && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install ${PIP_ARGS} . && cd ..

deps-e:
	pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements-dev.txt
	cd result && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install -e ${PIP_ARGS} . && cd ..
	cd core  && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install -e ${PIP_ARGS} . && cd ..
	cd client && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install -e ${PIP_ARGS} . && cd ..
	cd service && $(PYTHON_BIN) -m pip install ${PIP_ARGS} --index-url=https://nexus.int.svc.nect.com/repository/pypi-group/simple -r requirements.txt && pip install -e ${PIP_ARGS} . && cd ..

tests:
	cd result && $(PYTHON_BIN) -m pytest tests && cd ..
	cd core && $(PYTHON_BIN) -m pytest tests && cd ..
	cd client && $(PYTHON_BIN) -m pytest tests && cd ..
	cd service && $(PYTHON_BIN) -m pytest tests && cd ..

docker:
	echo "Building wheel for result ..."
	cd result && $(PYTHON_BIN) setup.py bdist_wheel && cd .. && echo "Success!"
	echo "Building wheel for core ..."
	cd core && $(PYTHON_BIN) setup.py bdist_wheel && cd .. && echo "Success!"
	mkdir -p service/deps service/deps/result service/deps/core
	cp result/dist/*.whl service/deps/result/ && cp core/dist/*.whl service/deps/core/
	cd service && docker build .

tox:
	cd result && tox && cd ..
	cd core && tox && cd ..
	cd client && tox && cd ..
	cd service && tox && cd ..

tox_clean:
	cd result && rm -rf .tox && cd ..
	cd core && rm -rf .tox && cd ..
	cd client && rm -rf .tox && cd ..
	cd service && rm -rf .tox && cd ..

.PHONY: deps deps-e tests docker tox tox_clean
