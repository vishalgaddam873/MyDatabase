import seed

db1 = seed.load('data/student1.db',True)
db2 = seed.load('data/extradata.db',True)

db1.set('firstName','Vishal')
db1.set('lastName','Gaddam')
db1.set('contact',5100220113)
db1.set('place','Mumbai')


db2.set('age',21)
db2.set('gender','Male')

a = db1.dmerge('data/extradata.db')
print(a)
