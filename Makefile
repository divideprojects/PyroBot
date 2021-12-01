test:
	@pre-commit run --all-files

run:
	@python3 -m pyrobot

clean:
	@pyclean .
