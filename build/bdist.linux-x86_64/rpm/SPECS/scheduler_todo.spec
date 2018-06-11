%define name scheduler_todo
%define version 0.0.14
%define unmangled_version 0.0.14
%define unmangled_version 0.0.14
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

Example with content

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


Example with content to modify done/undone

::

	update hit hoesung done

Example with content to modify date

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

Example with content

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
