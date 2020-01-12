# Library Management Python
### Simple Console App on Library Management with Python<br>
**Disclamier:** _I didn't made this from scratch. All rights to original Author(I don't know who is)<br>
Just fixed some errors. And made some tweaks_

## Prerequisite
At the time of making this project _`mysql-python-connector`_ only support Python v3.7.x
- Python v3.7.6
- MySQL Server v8.0.18 or above
- MySQL Workbench v8.0.18 or above
- Connector/Python (3.7) v8.0.18 or above

## Project Setup
Go through [this](https://www.youtube.com/watch?v=u96rVINbAUI "How To Install MySQL (Server and Workbench)") 
video. He has shown how to install MySQL Server and MySQL Workbench **but he didn't install Connector/Python so 
you have to add this yourself.**(You will understand ones you see the video)<br>
Also set the **password to `mysql`.** Since, this is the password used in the code.
<br>
If you followed the video you should be able to run SQL Queries. Execute these Queries.
```
create database library;
```
```
create table BookRecord (bno varchar(20), bname varchar(20), author varchar(20), price int, publisher varchar(20),qty int, d_o_purchase date);
```
Now, run LIBRARY MANAGEMENT.py file hopefully, you can now add and display books. 

---
### Work left to do
- create table for members from MySQL Workbench
- check the code for members
- check the code for book issues/return
