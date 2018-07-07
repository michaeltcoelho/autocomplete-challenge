.PHONY: clean
clean:
	@find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete

.PHONY: test
test:
	@pytest -s

.PHONY: cov
cov:
	@pytest --cov-report term-missing --cov=. tests/

.PHONY: run
run:
	@python manage.py
