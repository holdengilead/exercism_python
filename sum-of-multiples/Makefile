.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv sum_of_multiples_test.py
	mypy --strict sum_of_multiples.py
	/usr/local/bin/python3 -m pylint sum_of_multiples.py