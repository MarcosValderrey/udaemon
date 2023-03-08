test-suite-coverage:
	python -m coverage run -m unittest discover -s tests;
	python -m coverage report;
	python -m coverage html;
test-suite-run:
	python -m unittest discover -s tests;