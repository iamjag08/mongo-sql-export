import pymongo
from mongotriggers import MongoTrigger
from bson.json_util import dumps
import subprocess

'''
   Establish a connection to mongodb running on local machine as a container on port 27017.
   The user for mongo is test and password is test123.
   pymongo library is used to create a mongo connection object and return the same for subsequent use.
'''
def connectToMongoDB():
    #conn_str = "mongodb://test:test123@0.0.0.0/LibraryDB?retryWrites=true&w=majority&replicaSet=rs0"
    conn_str = "mongodb://test:test123@0.0.0.0:27017/LibraryDB?authSource=LibraryDB&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    try:
        print("Connected !!")
    except Exception:
        print("Unable to connect to the server.")
    return client

'''
 This is the callback function which will be invoked when a record is inserted to mongo,
 the function checks if the operation is insert, if not it skips further processing.
 If the operation is insert, then the new document is written to NewBook.json file and a shell script
 is invoked to import the json document.
'''
def notify_manager(op_document):
    if op_document["op"] != "i":
        print("Not an insert operation, skipping callback processing")
        return
    print ('wake up! A new book is added', op_document)
    with open('NewBook.json', 'w') as file:
        file.write(dumps(op_document["o"]))
    exit_code = subprocess.call('./insert.sh')
    print(exit_code)

'''
Export data from mongo container into a json file and then dumps it into mysql db using the shell script 'mysql-script.sh'
The script file also alters the table to create columns corresponding to the attributes in json document.
'''
def export_from_mongo():
    exit_code = subprocess.call('./mysql-script.sh')
    print(exit_code)

'''
Driver code which starts by connecting to mongo and defining a callback function to listen to operations 
on Books collection. Then the existing data from mongo is exported to mysql. Finally a document is inserted in mongo to 
demonstrate the working of the program. The record will be auto inserted into mysql once the callback handler is invoked.

'''
def watchAndExportData():
    client = connectToMongoDB()
    triggers = MongoTrigger(client)
    triggers.register_op_trigger(notify_manager, 'LibraryDB', 'Books')
    triggers.tail_oplog()
    export_from_mongo()
    client['LibraryDB']['Books'].insert_one({"ISBN": "978159876879","AccessionNo": 141220180089,"Title": "TestPython1","Edition": "Third","subtitle": "A Modern Introduction to Programming","Author": "Marijn Haverbeke","YearOfPublication": "2018","Publisher": "No Starch Press","Pages": 472,"Category": "Java","Price": 300})
    client['LibraryDB']['Books'].insert_one({"ISBN": "978159876879","AccessionNo": 141220180089,"Title": "TestPython2","Edition": "Third","subtitle": "A Modern Introduction to Programming","Author": "Marijn Haverbeke","YearOfPublication": "2018","Publisher": "No Starch Press","Pages": 472,"Category": "Java","Price": 300})
    print("Inserted!!!")

watchAndExportData()
