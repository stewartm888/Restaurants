# Restaurants
JSON/MongoDB tests


**General Notes**

MongoDB advantages?
- It stores data as JSON so you can use the same data clientside and serverside. This means you write almost no wiring code, everything just works.
- Flexible Schema. If your requirements change, you can adapt.
- Unstructured data - you can store and retrieve unstructured data easily. It's just JSON. Not every document in a collection needs the same fields.
- Denormalised data - Group related content in a single document.
- Clean and simple API - Mongo is nice to talk to.

MongoDB disadvantages?
- Denormalised data means no joins. If your data is highly relational, Mongo is not your baby. Your data is organised into collections. If you need data from more than collection, you need to hit the database more than once.
- Flexible schema means no built in data validation. Your data is validated at the application tier. The database is dumb and will store whatever your application gives it, even junk and typos.
- Bugs - Mongo is new and there are still issues in the tracker. Not bad bugs, but occasionally things don't work as you might expect.
- No transactions - A SQL database allows you to bundle multiple writes into a transaction. If one write fails the whole transaction is rolled back. Mongo lacks this feature, writes are small and atomic. If you need a transaction you must build it yourself.
- Theoretical data loss - Mongo scales using a technique called sharding. It creates slaves that mirror data written to the master. If the master goes down before data is mirrored you may lose recent commits depending on your settings.
