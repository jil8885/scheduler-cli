%define name scheduler_todo
%define version 0.0.9
%define unmangled_version 0.0.9
%define unmangled_version 0.0.9
%define release 1

Summary: A scheduler command line program in Python.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT LICENSE
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jeongin Lee <jil8885@hanynag.ac.kr>
Url: https://github.com/jil8885/scheduler-cli

%description
Scheduler-cli tool
================================
Intro
-----
Scheduler for Python

Installation
-----------------

::

	pip install scheduler-todo

Usage
-----------------

1. Add schedule
-------------------------------

::

	add {due} {content} in {category}

Example

::

	add 3/2 hit hoesung in school

Example without category

::

	add 3/2 hit hoesung


2. Delete schedule
----------------------------------

::

	delete all

::

	delete {index}

::

	delete in {category}

::

	delete done/undone

Example with index

::

	delete 3

Example with category

::

	delete in school


Example with state

::

	delete done


3. Update schedule
------------------------------

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
------------------------------------

::

	show {index}

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

	show 3

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

- v0.1 : Beta Version
- v0.2 : add calender func and fix input bugs
- v0.7 : add func to sync server

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
