.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv space_age_test.py
	mypy --strict space_age.py
	/usr/local/bin/python3 -m pylint space_age.py