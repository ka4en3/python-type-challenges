.PHONY: typing
typing:
	docker-compose run --rm type-checker bash -c "pyright src/"

.PHONY: build
build:
	docker-compose build

.PHONY: clean
clean:
	docker-compose down
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +