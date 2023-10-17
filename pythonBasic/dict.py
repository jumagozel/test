# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }

# car.update({"year":456})
# print(car)

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }
# car.pop("model", "color")
# print(car)

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }
# car.popitem()
# print(car)

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }
# del car["color"]
# print(car)

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }

# car.clear()
# print(car)

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }

# # for i in car.values():
# #     print(i)

# for i in car:
#     print(car[i])

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }

# for i in car:
#     print(i)
# print("---------------------------")
#  for in car.keys():
#    print(i)

# car={
#     "name":"BMW",
#     "model":"XS6",
#     "year": 2023,
#     "color": "grey",
#     "power": 3.5,
# }

# # for x in car.items():
# #     print(x)

# for x, y in car.items():
# #     print(x, y)

# users={
#     "user1":{
#         "name": "John",
#         "age": 22,
#         "email": "john@example.com"
#     },
#     "user2":{
#         "name":"Tom",
#         "age":28,
#         "email":"tom@example.com"
#     }
# }
# new=users["user1"].items()
# print(new)

# for i in users["user1"].items():
#     print(i)
# for i, c in users["user1"].items():
#     print(i, c)

# new1= users["user1"]["name"]
# new2= users["user1"]["age"]
# new3= users["user1"]["email"]
# print("users name:", new1, "\n users age:", new2, "\n users email:", new3)

print("Welcome travell service!!!!")

travell={
    "country1": {
        "USA": "Los Angeles",
        "JAPAN": "Tokyo",
        "TKM": "Ashgabat"
    },
    "country2": {
        "RUSSIAN": "Moscow",
        "CHINE": "Bejing",
        "GERMAN": "Berlin"
    },
    "country3": {
        "TURKIE": "istanbul",
        "FRANCE": "Paris",
        "ITALY": "Milano"
    },
}
for i in travell.keys():
    # print(travell[i])

    travell_list=list(travell[i])
    print(travell_list)

    selected=input("Selected Country: ")
    print(f"your selected country{travell['country1']}")