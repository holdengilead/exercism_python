.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv go_counting_test.py
	mypy --strict go_counting.py
	/usr/local/bin/python3 -m pylint go_counting.py