.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv connect_test.py
	mypy --strict connect.py
	/usr/local/bin/python3 -m pylint connect.py