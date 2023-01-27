.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv tree_building_test.py
	mypy --strict tree_building.py
	/usr/local/bin/python3 -m pylint tree_building.py