.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv gigasecond_test.py
	mypy --strict gigasecond.py
	/usr/local/bin/python3 -m pylint gigasecond.py