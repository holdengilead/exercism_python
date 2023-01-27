.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv all_your_base_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict all_your_base.py
	/usr/local/bin/python3.9 -m pylint all_your_base.py