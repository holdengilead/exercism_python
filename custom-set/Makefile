.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv custom_set_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict custom_set.py
	/usr/local/bin/python3.9 -m pylint custom_set.py