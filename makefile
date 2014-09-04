test:
	python -m tests.unit-tests

setup:
	pip install jinja2 pyflakes pep8
pep8:
	find . -name \*.py -exec pep8 --first --show-source --show-pep8 {} \;

pyflakes:
	find . -name \*.py -exec pyflakes {} \;
