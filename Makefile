.SHELLFLAGS: -ec

PYTHON = pipenv run python3

# Default make target
default:
	$(MAKE) help

# Installing PastaStore default packages from Pipfile
deps:
	@pipenv install

# Installing PastaStore develop and default packages from Pipfile
dev-deps:
	@pipenv install --dev

# Running PastaStore REST API in debug mode
debug: deps
	@echo "Starting PastaStore in debug mode.."
	@$(PYTHON) run.py --debug --env development

# Running PastaStore REST API
.PHONY: run
run: deps
	@echo "Starting PastaStore.."
	@$(PYTHON) run.py --env development

# Running PastaStore REST API
help: deps
	@$(PYTHON) run.py --help

# Removing the virtualenv created in deps make target
clean:
	@pipenv --rm

# Updating Pipfile.lock
lock: 
	@pipenv lock

# Launching the flake8 linter
run-linting: dev-deps
	@pipenv run flake8

# Launching the bandit secuirty linter
run-security-linting: dev-deps
	@pipenv run bandit -r . --configfile .bandit.yaml

# Running unit tests with pytest
test: dev-deps
	@pipenv run pytest
