# Setup

To install the required libraries, use pip install and the provided requirements.txt file.

	pip install -r requirements.txt




# Restaurants
JSON/MongoDB tests
http://nicholasjohnson.com/mongo/course/workbook/
https://www.journaldev.com/19392/python-xml-to-json-dict

**xml2json.py**
A handy python tool that converts XML files into a json object which is then written to a text file. Requires an .xml file and a .txt file in the active directory.  





---
Connecting to the terminal
We connect to the Mongo terminal using the mongo command
- mongo
By default Mongo will connect to localhost.

We can connect to a remote server by passing arguments, like so:
- mongo connection.mongolab.com:45352 -u username -p passw0rd
Once we connect to a Mongo instance we can type JavaScript directly into the console. We can create variables, do maths, write JSON.

---
Creating a database
We can switch to a database in Mongo with the use command.
- use petshop

This will switch to writing to the petshop database. It doesn't matter if the database doesn't exist yet. It will be brought into existence when you first write a document to it.

You can find which database you are using simply by typing db. You can drop the current database and everything in it using db.dropDatabase.
- db
- > petshop
- db.dropDatabase()

---
Collections
Collections are sets of (usually) related documents. Your database can have as many collections as you like. Because Mongo has no joins, a Mongo query can pull data from only one collection at a time. You will need to take this into account when deciding how to arrange your data. You can create a collection using the createCollection command.
- use petshop
- db.createCollection('mammals')
Collections will also be created automatically. If you write a document to a collection that doesn't exist that collection will be brought into being for you.

View your databases and collections using the show command, like this:
- show dbs
- show collections

---

Documents
Documents are JSON objects that live inside a collection. They can be any valid JSON format, with the caveat that they can't contain functions.

The size limit for a document is 16Mb which is more than ample for most use cases.

Creating a document
You can create a document by inserting it into a collection
- db.mammals.insert({name: "Polar Bear"})
- db.mammals.insert({name: "Star Nosed Mole"})

---

Finding a document
You can find a document or documents matching a particular pattern using the find function.

If you want to find all the mammals in the mammals collection, you can do this easily.
- db.mammals.find()


You can use find to:

Find a document by id
Find a user by email
Find a list of all users with the same first name
Find all cats who are more than 12 years old
Find all gerbils called 'Herbie' who are bald, have three or more eyes, and who have exactly 3 legs.
Limitations
You can't use find to chain complex operators. You can do a few simple things like counting, but if you want to real power you need the aggregate pipeline, which is actually not at all scary and is quite easy to use.

The Aggregate pipeline allows us to chain operations together and pipe a set of documents from one operation to the next.

You can use find with no arguments to list documents in a collection.
- db.entrycodes.find()

This will list all of the codes, 20 at a time.

You can get the same result by passing an empty object, like so:
- db.entrycodes.find({})

Assuming you know the object ID of a document. You can pull that document by id like so:
- db.entrycodes.find(ObjectId("557afc91c0b20703009f7edf"))

Say you have a list of users and you want to find by name, you might do:
- db.people.find({name: "dave"})

You can match on more than one field:
- db.people.find({
- >  name: "dave",
- >  email: "davey@aol.com"
- })


You can match on numbers:


---

**General Notes**

MongoDB advantages?
1. It stores data as JSON so you can use the same data clientside and serverside. This means you write almost no wiring code, everything just works.
2. Flexible Schema. If your requirements change, you can adapt.
3. Unstructured data - you can store and retrieve unstructured data easily. It's just JSON. Not every document in a collection needs the same fields.
4. Denormalised data - Group related content in a single document.
5. Clean and simple API - Mongo is nice to talk to.

MongoDB disadvantages?
1. Denormalised data means no joins. If your data is highly relational, Mongo is not your baby. Your data is organised into collections. If you need data from more than collection, you need to hit the database more than once.
2 Flexible schema means no built in data validation. Your data is validated at the application tier. The database is dumb and will store whatever your application gives it, even junk and typos.
3. Bugs - Mongo is new and there are still issues in the tracker. Not bad bugs, but occasionally things don't work as you might expect.
4. No transactions - A SQL database allows you to bundle multiple writes into a transaction. If one write fails the whole transaction is rolled back. Mongo lacks this feature, writes are small and atomic. If you need a transaction you must build it yourself.
5. Theoretical data loss - Mongo scales using a technique called sharding. It creates slaves that mirror data written to the master. If the master goes down before data is mirrored you may lose recent commits depending on your settings.
