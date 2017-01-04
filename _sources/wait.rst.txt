wait
====

In order to sync code execution with UI interaction you can use ``webium.wait.wait()`` method.
It is small wrapper over waiting library (https://pypi.python.org/pypi/waiting)
which handles WebDriverException which might occur during waiting time.
Provide predicate which should be calculated and method will do required sync.