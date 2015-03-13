#!/bin/bash
virtualenv ../docs_env
../docs_env/bin/pip install sphinx
../docs_env/bin/pip install sphinx-rtd-theme
rm -r ./html_docs/
../docs_env/bin/sphinx-build -b html ./docs/ ./html_docs/
