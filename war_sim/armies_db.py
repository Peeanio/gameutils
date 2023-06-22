import couchdb

couch = couchdb.Server("http://admin:mysecretpassword@localhost:5984/")

db = couch.delete('test')

db = couch.create('british_army')
