
build:
	python setup.py sdist --format=gztar
	twine upload dist/*
	# python setup.py bdist_wheel
	echo "Build Completed"
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf dat_struct_py/__pycache__
	rm -rf dat_struct_py/blocks/__pycache__
	rm -rf dat_struct_py/tests/__pycache__
	rm -rf .coverage
	rm -rf htmlcov
	echo "Cleanup Complete" 
test:
	coverage run setup.py test
	coverage html --omit="*datstructpyenv*,*test*,*init*,*setup*"
	echo "Tests Completed"
