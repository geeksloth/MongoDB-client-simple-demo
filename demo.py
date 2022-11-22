# import necessary packages
import pymongo
from time import sleep


def chapter(chapternumber=None, title=None, delay=5, line="-"*32):
    print()
    print(line)
    print("{}. {}".format(chapternumber, title))
    sleep(delay)

if __name__ == "__main__":
    print("Demo started.")
    chapter(1,"Creating a client object...", delay=2)
    # Connect to mongodb service, create a client object
    # Modify following values with your configurations
    myclient = pymongo.MongoClient(
        'localhost',
        username='root',
        password='mypassword',
        authMechanism='SCRAM-SHA-1'
    )
    print("OK")


    chapter(2, "Listing a databases.")
    print(myclient.list_database_names())


    chapter(3, "Create mydatabase.")
    mydb = myclient["mydatabase"]
    print("OK")


    chapter(4, "Listing a databases again.")
    print(myclient.list_database_names())


    chapter(5, "Create a collection")
    mycol = mydb["customers"]
    print(myclient.list_database_names())


    chapter(6, "Listing collections")
    print(mydb.list_collection_names())


    chapter(7, "Check if collection exist.")
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")


    chapter(8, "Insert a record to customers collection.")
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)
    print(x)


    chapter(9, "Find one doc.")
    x = mycol.find_one()
    print(x)


    chapter(10, "Insert multiple docs.")
    mylist = [
        { "name": "Amy", "address": "Apple st 652"},
        { "name": "Hannah", "address": "Mountain 21"},
        { "name": "Michael", "address": "Valley 345"},
        { "name": "Sandy", "address": "Ocean blvd 2"},
        { "name": "Betty", "address": "Green Grass 1"},
        { "name": "Richard", "address": "Sky st 331"},
        { "name": "Susan", "address": "One way 98"},
        { "name": "Vicky", "address": "Yellow Garden 2"},
        { "name": "Ben", "address": "Park Lane 38"},
        { "name": "William", "address": "Central st 954"},
        { "name": "Chuck", "address": "Main Road 989"},
        { "name": "Viola", "address": "Sideway 1633"}
    ]
    x = mycol.insert_many(mylist)
    print(x.inserted_ids)


    chapter(11, "Find all docs.")
    for x in mycol.find():
        print(x)


    chapter(12, "Insert multiple docs with specific ids.")
    mylist = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]
    x = mycol.insert_many(mylist)
    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)


    chapter(13, "Find all docs (again).")
    for x in mycol.find():
        print(x)


    chapter(14, "Return only some fields.")
    for x in mycol.find({},{ "_id": 0, "name": 1, "address": 0 }):
        print(x)


    chapter(15, "Query.")
    myquery = { "address": "Park Lane 38" }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)


    chapter(16, "Query address from S and greater.")
    myquery = { "address": { "$gt": "S" } }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)


    chapter(17, "Filter with regular expressions, address starts with S")
    myquery = { "address": { "$regex": "^S" } }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)


    chapter(18, "Sort the result.")
    mydoc = mycol.find().sort("name") # sort ascending
    # mydoc = mycol.find().sort("name", -1) # sort descending
    for x in mydoc:
        print(x)



    chapter(19, "Delete doc with Mountain 21 address.")
    myquery = { "address": "Mountain 21" }
    mycol.delete_one(myquery)
    for x in mycol.find():
        print(x)


    chapter(20, "Delete docs start with S.")
    myquery = { "address": {"$regex": "^S"} }
    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")


    chapter(21, "Find all docs (again).")
    for x in mycol.find():
        print(x)


    chapter(22, "Update a coll, change address from 'Valley 345' to 'Canyon 123'.")
    myquery = { "address": "Valley 345" }
    newvalues = { "$set": { "address": "Canyon 123" } }
    #x = mycol.update_one(myquery, newvalues)
    #print(x.modified_count, "documents updated.")
    #print "customers" after the update:
    for x in mycol.find():
        print(x)


    chapter(23, "Update many.")
    myquery = { "address": { "$regex": "^S" } }
    newvalues = { "$set": { "name": "Minnie" } }
    x = mycol.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    #print "customers" after the update:
    for x in mycol.find():
        print(x)


    chapter(24, "Find and limit the result to 5 docs.")
    myresult = mycol.find().limit(5)
    for x in myresult:
        print(x)


    chapter(25, "Delete all docs.")
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")


    chapter(26, "Find all docs (again).")
    for x in mycol.find():
        print(x)


    chapter(27, "Drop the collection.")
    print("before: ")
    print(mydb.list_collection_names())
    mycol.drop()
    print("after: ")
    print(mydb.list_collection_names())

    chapter(28, "End of demonstration.")
    print("OK")