build-wheel:
	python setup.py bdist_wheel --universal

build-tar-gz:
	python setup.py sdist

clean:
	rm -rf dist/ build/ Vaka_Avto.egg-info

.PHONY: clean build-tar-gz build-wheel