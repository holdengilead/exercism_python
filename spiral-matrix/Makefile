.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv spiral_matrix_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict spiral_matrix.py
	/usr/local/bin/python3.9 -m pylint spiral_matrix.py