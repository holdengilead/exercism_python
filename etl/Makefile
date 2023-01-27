.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv etl_test.py
	mypy --strict etl.py
	/usr/local/bin/python3 -m pylint etl.py