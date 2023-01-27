.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv darts_test.py
	mypy --strict darts.py
	/usr/local/bin/python3 -m pylint darts.py