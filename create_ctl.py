#!/usr/bin/python

import os

FILE_NAME="loader_file_1.dat"

delimeter=","
with open(FILE_NAME) as fp:
	header = fp.readline().strip().split(delimeter)
num_of_columns=header.__len__()
table_name=FILE_NAME.strip().split(".")[0]
create_table_staement="CREATE TABLE TMP_"+table_name+" ( "
ctl_statement="load data \nappend \ninto table " + table_name + " \nfields terminated by " + "\",\" \nTRAILING NULLCOLS(" 
i=1
for columns in header:
	create_table_staement += "\n"
	create_table_staement += columns + " VARCHAR(50)"
	ctl_statement += "\n"
	ctl_statement += columns + " VARCHAR(50)"
	 
	if i < num_of_columns:
		create_table_staement += ","
		ctl_statement += ","
	i+=1
	

create_table_staement += ");"
ctl_statement += ");"

fp = open(table_name+".ctl",'w')
fp.write(ctl_statement)
fp.close()

fp = open(table_name+"_create.sql",'w')
fp.write(create_table_staement)
fp.close()

command1="sed -i '1d' " + FILE_NAME +  "_FINAL"
command2="cp " + FILE_NAME + " " + FILE_NAME + "_FINAL"

os.system(command2)
os.system(command1)
