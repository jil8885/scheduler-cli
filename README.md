Scheduler-cli tool
================================
Intro
-----
Scheduler for Python


Build Status
-----------------
[![Build Status](https://travis-ci.org/jil8885/scheduler-cli.svg?branch=master)](https://travis-ci.org/jil8885/scheduler-cli)



Installation
-----------------

	pip install scheduler-cli
	



add schedule
-----------------

	add with category             - add {due} {content} in {category}   ex) add 3/2 homework in assignment
	add without category          - add {due} {content}                 ex) add 3/2 homework



delete schedule
-----------------

	delete all schedule            - delete all
	delete schedule with index     - delete {index}                     ex) delete 1
	


update state of schedule
-----------------

	update state with index        - update {index} {done/undone}        ex) update 3 done / update 3 undone 
	update due date with index     - update {index} at {due}             ex) update 3 at 7/1
	
	update state with category     - update in {index} {done/undone}     ex) update in assignment done / update in assignment undone
	update due date with category  - update in {index} at {due}          ex) update in assignment at 7/1
	
	
	
show schedules
-----------------
	
	get all schedule                - show all                            ex) show all
	get schedule with index         - show {index}                        ex) show 3
	get all schedule in category    - show in {category}                  ex) show in assignment
	get all schedule at month       - show in {month}                     ex) show at july (not a number)



