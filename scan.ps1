trap
{
	deactivate
	rmvirtualenv webium
	write-output $_
	exit 1
}

Import-Module virtualenvwrapper
mkvirtualenv webium

pip install pep8==1.5.6
if ($LastExitCode -ne 0) {
    throw "Failed to install pep8"
}

pip install -e .
if ($LastExitCode -ne 0) {
    throw "Failed to install webium with all required packages"
}

pep8 --ignore=E501 .
if ($LastExitCode -ne 0) {
    throw "There are pep8 errors with webium"
}

python ./run_tests.py
if ($LastExitCode -ne 0) {
    throw "Tests are failed"
}
