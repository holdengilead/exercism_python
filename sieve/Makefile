.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv sieve_test.py
	mypy --strict sieve.py
	/usr/local/bin/python3 -m pylint sieve.py