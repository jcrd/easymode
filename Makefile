start: node_modules
	npm run start

build: node_modules
	npm run build:css

node_modules:
	npm ci

.PHONY: start build
