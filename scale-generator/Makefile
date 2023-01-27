.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv scale_generator_test.py
	mypy --strict scale_generator.py
	/usr/local/bin/python3 -m pylint scale_generator.py