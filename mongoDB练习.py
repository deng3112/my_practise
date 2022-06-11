import pymongo
clcient = pymongo.MongoClient(host='localhost', port=27017)


# clcient = MongoClient('mongodb://localhost:27017/')

db = clcient['test']
collection = db.students
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result.inserted_ids)
result = collection.find_one({'name':'Mink'})
print(type(result))
print(result)