test:
	coverage run -m unittest
	coverage report --omit=env/lib/python3.6/site-packages/colorama/*

.PHONY: test
