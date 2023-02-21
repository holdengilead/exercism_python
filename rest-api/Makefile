.PHONY: test

test:
	pytest -vv rest_api_test.py
	mypy --strict *.py
	pylint rest_api.py