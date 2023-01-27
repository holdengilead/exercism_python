.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv flatten_array_test.py
	mypy --strict flatten_array.py
	/usr/local/bin/python3 -m pylint flatten_array.py