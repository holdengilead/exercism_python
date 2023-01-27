.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv list_ops_test.py
	mypy --strict list_ops.py
	/usr/local/bin/python3 -m pylint list_ops.py