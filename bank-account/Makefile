.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv bank_account_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict bank_account.py
	/usr/local/bin/python3.9 -m pylint bank_account.py