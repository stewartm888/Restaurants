# Restaurants
JSON/MongoDB tests
http://nicholasjohnson.com/mongo/course/workbook/


Creating a database
We can switch to a database in Mongo with the use command.
      use petshop

This will switch to writing to the petshop database. It doesn't matter if the database doesn't exist yet. It will be brought into existence when you first write a document to it.

You can find which database you are using simply by typing db. You can drop the current database and everything in it using db.dropDatabase.
      db
      > petshop
      db.dropDatabase()


Collections
Collections are sets of (usually) related documents. Your database can have as many collections as you like. Because Mongo has no joins, a Mongo query can pull data from only one collection at a time. You will need to take this into account when deciding how to arrange your data.


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
