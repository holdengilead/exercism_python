.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv complex_numbers_test.py
	mypy --strict complex_numbers.py
	/usr/local/bin/python3 -m pylint complex_numbers.py