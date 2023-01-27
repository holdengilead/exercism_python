.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv grep_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict grep.py
	/usr/local/bin/python3.9 -m pylint grep.py