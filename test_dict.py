infos = {
    "name": "wiwid",
    "age": 25,
    "gender": "male",
    "hobby": "coding",
    "address": "jakarta",
}

infos['status'] = "menikah"
print(infos)
print("status" in infos)
del(infos['status'])
print(infos)
# print(infos["name"])
# print(infos["age"])
# print(infos["gender"])
# print(infos["hobby"])
# print(infos["address"])

for key, value in infos.items():
    print(key, value)