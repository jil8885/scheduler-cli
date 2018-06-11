Scheduler-cli tool
================================
Intro
-----
Scheduler for Python

Installation
-----------------
As a Python Module
::

	pip install scheduler-todo

As a Debian Package
::

	sudo dpkg -i <file name>.deb

As a RedHat Package
::

	rpm -Uvh <file name>.rpm

Usage
-----------------

1. Add schedule
-------------------------------

::

	add {due} {content} in {category}

Example

::

	add 2018/3/2 hit hoesung in school

Example without category

::

	add 2018/3/2 hit hoesung


2. Delete schedule
----------------------------------

::

	delete all

::

	delete {content}

::

	delete in {category}

::

	delete done/undone

Example with index

::

	delete hit hoesung

Example with category

::

	delete in school


Example with state

::

	delete done


3. Update schedule
------------------------------

::

	update {content} {done/undone}

::

	update {content} at {date to modify}


Example with index to modify done/undone

::

	update hit hoesung done

Example with index to modify date

::

	update hit hoesung at 5/31

Example with category to modify done/undone

::

	update in school done

Example with category to modify date

::

	update in school at 6/31



4. Print schedule
------------------------------------

::

	show {content}

::

	show in {category}

::

	show at {month}

::

	show {done/undone}
	
Example with showing all schedule

::

	show all

Example with index

::

	show hit hoesung

Example with category

::

	show in school

Example with month

::

	show at May

Example with state

::

	show undone

5. Pull schedule from server

::

	pull


6. Pull schedule to server

::

	push

7. Sync schedule with server

::

	sync


	
Changelog
-----------

- v0.0.1 : Beta Version
- v0.0.2 : add calender func and fix input bugs
- v0.0.7 : add func to sync server
- v0.1.0 : Last Pre-release