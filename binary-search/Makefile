.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv binary_search_test.py
	mypy --strict binary_search.py
	/usr/local/bin/python3 -m pylint binary_search.py