.SHELLFLAGS: -ec

# Installing PastaStore dependencies
deps:
	@pipenv install

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