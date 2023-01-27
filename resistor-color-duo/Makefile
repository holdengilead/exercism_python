.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv resistor_color_duo_test.py
	mypy --strict resistor_color_duo.py
	/usr/local/bin/python3 -m pylint resistor_color_duo.py