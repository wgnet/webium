#!/usr/bin/env bash
virtualenv ../venv || exit 1

../venv/bin/pip install pep8==1.5.6 nose==1.3.3 || exit 1
../venv/bin/pip install -e . || exit 1
../venv/bin/pep8 --ignore=E501 . || exit 1
../venv/bin/python ./run_tests.py