.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xv saddle_points_test.py
	mypy saddle_points.py
	/usr/local/bin/python3 -m pylint saddle_points.py