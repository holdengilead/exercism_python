.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv grains_test.py
	mypy grains.py
	/usr/local/bin/python3 -m pylint grains.py