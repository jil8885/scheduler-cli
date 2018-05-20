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





3. Update schedule
-----------

::

	update {index} {done/undone}

::

	update {index} at {date to modify}


Example with index to modify done/undone

::

	update 3 done

Example with index to modify date

::

	update 3 at 5/31

Example with category to modify done/undone

::

	update in school done

Example with category to modify date

::

	update in school at 6/31



4. Print schedule
-----------

::

	show {index}

::

	show in {category}

::

	show at {month}

Example with showing all schedule

::

	show all

Example with index

::

	show 3

Example with category

::

	show in school

Example with month

::

	show at May
Changelog
-----------

- v0.1 : Beta Version
- v0.2 : add calender func and fix input bugs