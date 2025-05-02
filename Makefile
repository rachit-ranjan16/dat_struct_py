.PHONY: build clean test coverage install dev dist

install:
	pip install -e .

dev:
	pip install -e ".[dev]"
	pip install pytest pytest-cov build twine

test:
	python -m pytest
	echo "Tests Completed"

dist:
	pip install --upgrade build
	python3 -m build

build: clean dist
	pip install --upgrade twine
	twine check dist/*

upload: build
	twine upload dist/*

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf dat_struct_py/__pycache__
	rm -rf dat_struct_py/blocks/__pycache__
	rm -rf dat_struct_py/tests/__pycache__
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
