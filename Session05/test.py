person = {"name": "cuong",
"length":20,
"ex": ["a","d"]}
print(person)
person["chim to"] = 123
print(person)
del person["chim to"]
print(person)
print(len(person))
key = 'length'
if key in person:
    print(person[key])
else:
    print("not found")
print()
for k in person:
    print(k, person[k])

for key, value in person.items():
    print(key, value)

for value in person.values():
    print(value)