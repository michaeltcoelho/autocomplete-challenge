
.PHONY: test
test:
	@pytest -s

.PHONY: cov
cov:
	@pytest --cov-report term-missing --cov=. tests/

.PHONY: run
run:
	@python manage.py
