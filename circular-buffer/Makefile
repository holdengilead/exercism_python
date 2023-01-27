.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv circular_buffer_test.py
	mypy --strict circular_buffer.py
	/usr/local/bin/python3 -m pylint circular_buffer.py