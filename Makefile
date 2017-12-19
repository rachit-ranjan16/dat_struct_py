VERSION = 1.0.0
#HOST=127.0.0.1
#TEST_PATH=./

build:
	python setup.py sdist --format=gztar
	python setup.py bdist_wheel
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info 


