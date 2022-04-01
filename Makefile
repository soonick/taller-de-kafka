build:
	docker-compose build
.PHONY: build

start: build
	docker-compose up
.PHONY: start
