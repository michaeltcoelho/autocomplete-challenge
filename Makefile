.PHONY: clean
clean:
	@find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete

.PHONY: install
install:
	@pip install -r requirements.txt

.PHONY: test
test:
	@pytest --cov-report term-missing --cov=. tests/

.PHONY: run
run:
	@python manage.py
