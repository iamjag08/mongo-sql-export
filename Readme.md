<!-- ABOUT THE PROJECT -->
## About The Project

This objective of this project is to demonstrate data sync between MongoDB and SQL. We create a mongo database and collection. Some records will be inserted into mongo collection.
Then this data will be exported to mysql using a script, such that there will be separate columns for each attribute in the document.
The next task is to listen to subsequent inserts on mongo collection and sync this data to mysql table automatically.

### Getting started


### Prerequisites

Docker must be installed in the system. Open terminal, clone this repository and switch to mongo-sql-export directory.

### Steps

1. run ```docker compose up -d```
2. run mongo as a replica,
```docker exec db mongo --eval "rs.initiate({_id : 'rs0',members: [{ _id : 0, host : \"db:27017\" }]})" ```
3. run ```docker exec -it db bash```
4. in the shell, type mongo
5. Now we are in mongo shell and we can start creating db and collections
6. ```use LibraryDB```
7. ```db.createCollection('Books')```
8. Now the database and collection is created, we can insert some documents in the collection.
``` db.Books.insertMany([{"ISBN": "9781593279509","AccessionNo": 141220180001,"Title": "A Modern Introduction to Programming","Edition": "Third","subtitle": "A Modern Introduction to Programming","Author": "Marijn Haverbeke","YearOfPublication": "2018","Publisher": "No Starch Press","Pages": 472,"Category": "Java","Price": 300	},	{"ISBN": "9781593279508","AccessionNo": 241220150002,"Title": "Programming In ANSI C","Edition": "Eighth","Author": "E Balaguruswamy","YearOfPublication": "2015","Publisher": "McGraw Hill","Pages": 450,"Category": "C","Price": 600	},	{"ISBN": "9781593279507","AccessionNo": 160420200003,"Title": "Let Us C","Edition": "Seventeenth","Author": "Yashavant Kanetkar ","YearOfPublication": "2020","Publisher": "McGraw Hill","Pages": 600,"Category": "C","Price": 330	},	{"ISBN": "9781593279506","AccessionNo": 200820190004,"Title": "Programming with Java","Edition": "Sixth","Author": "E Balaguruswamy","YearOfPublication": "2019","Publisher": "McGraw Hill","Pages": 600,"Category": "Java","Price": 480	},	{"ISBN": "9781593279505","AccessionNo": 210820170005,"Title": "Fundamentals of Database Systems","Edition": "Sixth","Author": "Elmasri Ramez, Navathe Shamkant","YearOfPublication": "2017","Publisher": "Pearson","Pages": 1100,"Category": "DBMS","Price": 850	},	{"ISBN": "9781593279505","AccessionNo": 100820210006,"Title": "Database System Concepts","Edition": "Seventh","Author": "Abraham Silberschatz","YearOfPublication": "2021","Publisher": "McGraw Hill","Pages": 1000,"Category": "DBMS","Price": 900	},	{"ISBN": "9781593279505","AccessionNo": 181020200007,"Title": "python programming","Edition": "Seventh","Author": "Tony F Charles","YearOfPublication": "2020","Publisher": "Tony F Charles","Pages": 330,"Category": "Python","Price": 1725	},	{"ISBN": "9781593279508","AccessionNo": 101220160008,"Title": "Head First Python: A Brain-Friendly Guide","Edition": "Second","Author": "Paul Barry","YearOfPublication": "2016","Publisher": "O'REILLY","Pages": 624,"Category": "Python","Price": 1275	},	{"ISBN": "9781593279509","AccessionNo": 290920160006,"Title": "Effective Java","Edition": "Second","Author": "Joshua Bloch","YearOfPublication": "2016","Publisher": "","Pages": 264,"Category": "Java","Price": 344	},	{"ISBN": "9781593279510","AccessionNo": 101220200010,"Title": "Java The Complete Reference","Edition": "Eleventh","Author": "Herbert Schildt","YearOfPublication": "2020","Publisher": "McGraw Hill","Pages": 924,"Category": "Java","Price": 1248	}])```
  This will insert 10 records into Books collection.
9. Install pymongo by running ```python3 -m pip install 'pymongo[srv]'```
10. Install mysql database on local machine, by default root user won't have any password and it can be connected from localhost.
11. Create the database LibraryDB in mysql.
12. Run the script solution-q1.py by the command ```python solution-q1.py```
13. Switch to LibraryDB in mysql and run the query ```select Edition,price,Title from Books;```
14. There should be rows corresponding to mongo entries and columns corresponding to attributes.
The entries with title 'TestPython1' and 'TestPython2' are the ones dynamically inserted into mongo by the program after the data is exported.
These entries are now visible in mysql table because the callback function was watching the inserts happening on mongo and then it inserted those records to mysql via the shell script insert.sh.


