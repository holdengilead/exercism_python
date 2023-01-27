.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv yacht_test.py
	mypy --strict yacht.py
	/usr/local/bin/python3 -m pylint yacht.py