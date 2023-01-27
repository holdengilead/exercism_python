.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv say_test.py
	mypy --strict say.py
	/usr/local/bin/python3 -m pylint say.py