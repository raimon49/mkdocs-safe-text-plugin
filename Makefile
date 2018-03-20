SRC_DIR='mkdocssafetext'
DEV_DEPENDS='dev-requirements'

.DEFAULT: help
.PHONY: help
help:
	@echo 'Usage: make <subcommand>'
	@echo ''
	@echo 'Subcommands:'
	@echo '    setup          Setup for development'
	@echo '    local-install  Install locally'
	@echo '    update-depends Re-compile requirements for development'
	@echo '    test           Run unittests'
	@echo '    deploy         Release to PyPI server'
	@echo '    test-deploy    Release to Test PyPI server'
	@echo '    build          Build package'
	@echo '    clean          Clean directories'

.PHONY: setup
setup:
	pip install -r $(DEV_DEPENDS).txt

.PHONY: local-install
local-install:
	pip install -e .

.PHONY: update-depends
update-depends:
	pip-compile -U $(DEV_DEPENDS).in

.PHONY: test
test:
	python setup.py test

.PHONY: deploy
deploy: build
	twine upload dist/*

.PHONY: test-deploy
test-deploy: build
	twine upload -r pypitest dist/*

.PHONY: build
build: clean
	python setup.py sdist bdist_wheel

.PHONY: clean
clean:
	find $(SRC_DIR) -name "*~" -or -name "*.swp" -or -name "*.pyc" | xargs --no-run-if-empty rm
	rm -rf dist

