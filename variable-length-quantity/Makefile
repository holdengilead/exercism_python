.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv variable_length_quantity_test.py
	mypy --strict variable_length_quantity.py
	/usr/local/bin/python3 -m pylint variable_length_quantity.py