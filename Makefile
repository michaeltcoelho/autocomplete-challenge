
.PHONY: test
test:
	@pytest -s

.PHONY: cov
cov:
	@pytest --cov=. tests/
