.PHONY: test

test:
	/usr/local/bin/python3.9 -m pytest -vv rail_fence_cipher_test.py
	/usr/local/Cellar/python@3.9/3.9.7_1/Frameworks/Python.framework/Versions/3.9/bin/mypy --strict rail_fence_cipher.py
	/usr/local/bin/python3.9 -m pylint rail_fence_cipher.py