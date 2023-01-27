.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv matching_brackets_test.py
	mypy --strict matching_brackets.py
	/usr/local/bin/python3 -m pylint matching_brackets.py