.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv diamond_test.py
	mypy --strict diamond.py
	/usr/local/bin/python3 -m pylint diamond.py