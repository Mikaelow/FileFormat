# FileFormat
Script to format sql file to pandas for me to speed up my coding.  
Feel free to use it all u need to do is paste in txt ur sql code then launch main.py in your compiler.

Example
insert into Students (student_id, student_name) values ('1', 'Alice')
insert into Students (student_id, student_name) values ('2', 'Bob')
insert into Students (student_id, student_name) values ('13', 'John')
insert into Students (student_id, student_name) values ('6', 'Alex')

Output
Students
['1', 'Alice'],
['2', 'Bob'],
['13', 'John'],
['6', 'Alex'],
