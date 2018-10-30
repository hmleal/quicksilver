help:
	@echo "Makefile for quicksilver web framework                             "
	@echo "                                                                   "
	@echo "Usage:                                                             "
	@echo "    test                                      Run all project tests"

test:
	@py.test tests --cov=quicksilver --pep8 --flakes
