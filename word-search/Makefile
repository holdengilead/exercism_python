.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv word_search_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict word_search.py
	/usr/local/bin/python3.9 -m pylint word_search.py