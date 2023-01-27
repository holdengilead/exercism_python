.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv react_test.py
	mypy --strict react.py
	/usr/local/bin/python3 -m pylint react.py