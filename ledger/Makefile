.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv ledger_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict ledger.py
	/usr/local/bin/python3.9 -m pylint ledger.py