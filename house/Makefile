.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv house_test.py
	mypy --strict house.py
	/usr/local/bin/python3 -m pylint house.py