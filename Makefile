test:
	coverage run -m unittest
	coverage report

.PHONY: test
