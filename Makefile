# Makefile for kiss
#
# Source:: https://github.com/ampledata/kiss
# Author:: Greg Albrecht <gba@splunk.com>
# Copyright:: Copyright 2013 OnBeep, Inc.
# License:: Apache License 2.0
#


init:
	pip install -r requirements.txt --use-mirrors

lint:
	pylint -f parseable -i y -r y kiss/*.py tests/*.py *.py | \
		tee pylint.log

cli_lint:
	pylint -f colorized -i y -r n kiss/*.py tests/*.py *.py

flake8:
	flake8 --exit-zero  --max-complexity 12 kiss/*.py tests/*.py *.py | \
		awk -F\: '{printf "%s:%s: [E]%s\n", $$1, $$2, $$3}' | tee flake8.log

cli_flake8:
	flake8 --max-complexity 12 kiss/*.py tests/*.py *.py

pep8: flake8

clonedigger:
	clonedigger --cpd-output .

install:
	pip install .

uninstall:
	pip uninstall kiss

develop:
	python setup.py develop

publish:
	python setup.py register sdist upload

nosetests:
	python setup.py nosetests

test: init lint flake8 clonedigger nosetests

clean:
	rm -rf *.egg* build dist *.pyc *.pyo cover doctest_pypi.cfg nosetests.xml \
		pylint.log *.egg output.xml flake8.log */*.pyc */*.pyo
