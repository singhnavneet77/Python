info={
    "name":"Navneet",
    "age":20,
    "subject":["C","C++","Python"],
    "class":("Second year","sec->A")
}
# print(info)

student={
    "name":"Tom",
    "subject":{
        "math":4.5,
        "phy":4,
        "chem":4.75
    }
}
# print(student["subject"]["math"])

#Set in Python
#Set is unordered.
collection={1,2,3,4}#It's ignore the duplicate value.
cool={1,2,3,"good","night"}#It is also allowed.
# print(collection)
# print(type(collection))
# print(cool)
#For creating empty set
dog2={1,2,3,4}
dog=set()
dog.add(1)
dog.add(2)
dog.add(2)
print(dog.union(dog2))
