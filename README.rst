Scheduler-cli tool
================================
Intro
-----
Scheduler for Python

Installation
-----------------

::

	pip install scheduler-cli

Usage
-----------------

1. Add schedule
-----------

::

	add {due} {content} in {category}

Example

::

	add 3/2 hit hoesung in school

Example without category

::

	add 3/2 hit hoesung

1. Delete schedule
-----------

::

	delete {index}

::

	delete {category}

Example with deleting all schedule

::

	delete all

Example with index

::

	delete 3

Example with category

::

	delete in school
Changelog
-----------

- v0.1 : Beta Version
- v0.2 : add calender func and fix input bugs