.SHELLFLAGS: -ec

# Installing PastaStore default packages from Pipfile
deps:
	@pipenv install

# Installing PastaStore develop and default packages from Pipfile
dev-deps:
	@pipenv install --dev

# Running PastaStore REST API
.PHONY: run
run: deps
	@echo "Starting PastaStore.."
	@pipenv run python3 run.py

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
	@pipenv run bandit -r .