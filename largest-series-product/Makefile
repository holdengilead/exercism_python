.PHONY: test

test:
	/usr/local/bin/python3 -m pytest -xvv largest_series_product_test.py
	mypy --strict largest_series_product.py
	/usr/local/bin/python3 -m pylint largest_series_product.py