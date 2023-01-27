.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv sublist_test.py
	mypy --strict sublist.py
	/usr/local/bin/python3 -m pylint sublist.py