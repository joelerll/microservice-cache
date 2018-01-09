all: config

microservice:
	python microservice/server.py

gateway:
	node gateway.js

install:
	./scripts/install_root_add

config:
	./scripts/install

.PHONY: config install gateway microservice