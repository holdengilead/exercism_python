.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -vv robot_simulator_test.py
	mypy --strict robot_simulator.py
	/usr/local/bin/python3 -m pylint robot_simulator.py