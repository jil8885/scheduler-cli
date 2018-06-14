Scheduler-cli tool
================================
Intro
-----
Scheduler for Python


Build Status
-----------------

Travis CI


[![Build Status](https://travis-ci.org/jil8885/scheduler-cli.svg?branch=master)](https://travis-ci.org/jil8885/scheduler-cli)

Wercker

[![wercker status](https://app.wercker.com/status/a733759cfdcbf378d1d116d64c78b8e2/s/master "wercker status")](https://app.wercker.com/project/byKey/a733759cfdcbf378d1d116d64c78b8e2)


Codeship

[![Codeship Status for codeship/documentation](https://codeship.com/projects/0bdb0440-3af5-0133-00ea-0ebda3a33bf6/status?branch=master)](https://codeship.com/projects/293979)


Installation
-----------------

	pip install scheduler-todo
	



add schedule
-----------------

	add with category             - add {due} {content} in {category}   ex) add 2018/3/2 homework in assignment
	add without category          - add {due} {content}                 ex) add 2018/3/2 homework



delete schedule
-----------------

	delete all schedule            - delete all
	delete schedule with content     - delete {content}                     ex) delete hit hoesung
	


update state of schedule
-----------------

	update state with content        - update {content} {done/undone}        ex) update homework done / update homework undone 
	update due date with content     - update {content} at {due}             ex) update english homework at 7/1
	
	update state with category     - update in {content} {done/undone}     ex) update in assignment done / update in assignment undone
	update due date with category  - update in {content} at {due}          ex) update in assignment at 7/1
	
	
	
show schedules
-----------------
	
	get all schedule                - show all                            ex) show all
	get schedule with content         - show {content}                        ex) show homework
	get all schedule in category    - show in {category}                  ex) show in assignment
	get all schedule at month       - show in {month}                     ex) show at july (not a number)


update from the server
------------------------

	pull schedule from server       - pull
	push schedule to server         - push
	sync schedule with server	- sync


You can use this module directly from terminal through command starts with scheduler-cli

You can start calender sync server with command 'scheduler-server'
You can start calender slack bot server with command 'scheduler-slack'
