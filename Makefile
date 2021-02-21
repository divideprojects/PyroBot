test:
	@pre-commit run --all-files

install:
	@python3 -m pip install --upgrade pip setuptools
	@python3 -m pip install --upgrade -r requirements.txt

dev-install:
	@python3 -m pip install --upgrade pip setuptools
	@python3 -m pip install --upgrade -r requirements-dev.txt
	@sleep 5
	@pre-commit

run:
	@python3 -m pyrobot
