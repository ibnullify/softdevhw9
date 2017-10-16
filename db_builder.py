#Ibnul Jahan
#HW09 -- No Treble
#Software Development Pd7
#2017-10-15

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


#==========================================================
#MAKE ALL FUNCTIONS HERE
def make_table(table_name, table_cols):
    return "CREATE TABLE " + table_name + " (" + table_cols + ")"

#populates the peeps table
def populate_peeps():
    peeps_csv = open('peeps.csv', 'rU')
    peeps = csv.DictReader(peeps_csv)
    for row in peeps:
	ID = row['id']
	name = row['name']
	age = row['age']
	command = "INSERT INTO peeps VALUES("+ ID + ",'" + name + "'," + age + ")"
        c.execute(command) #adds student to table
    peeps_csv.close()

#populates the courses table
def populate_courses():
    courses_csv = open('courses.csv', 'rU')
    courses = csv.DictReader(courses_csv)
    for row in courses:
	ID = row['id']
	code = row['code']
	mark = row['mark']
	command = "INSERT INTO courses VALUES("+ ID + ",'" + code + "'," + mark + ")"
	c.execute(command) #adds course to table
    courses_csv.close()


#==========================================================
#CALL EVERYTHING HERE

#makes courses table
command = make_table("courses", "code TEXT, mark INTEGER, id INTEGER")
c.execute(command)
#makes peep table
command = make_table("peeps", "name TEXT, age INTEGER, id INTEGER")         #put SQL statement in this string
c.execute(command)      #run SQL statement
#populates them
populate_peeps()
populate_courses()


#==========================================================
db.commit() #save changes
db.close()  #close database


