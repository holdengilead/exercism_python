.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv transpose_test.py
	mypy --strict transpose.py
	/usr/local/bin/python3 -m pylint transpose.py