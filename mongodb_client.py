from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['nf_central']

# quote collection, store 100000 pdfs into mongodb
quote = db.quote
for i in range(100000):
	with open('samples.pdf',"rb") as fp:
		data = fp.read()
		document_id = quote.insert_one({"data": data})
		print(document_id)
		fp.close()
quote.delete_many({})

# user collection, insert into 20000 users
user = db.user
for i in range(20000):
	email = "a"+ str(i) + "@alpha.com"
	user.insert_one({"email":email, "instance":i})
