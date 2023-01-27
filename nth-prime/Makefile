.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv nth_prime_test.py
	mypy --strict nth_prime.py
	/usr/local/bin/python3 -m pylint nth_prime.py