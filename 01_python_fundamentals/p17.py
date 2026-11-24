customer = {
    "name":"John",
    "age":21,
    "city":"California"
    }


# print(customer)
# print(customer["name"])
# print(customer.keys())
# print(customer.values())
# print(customer.items())
# print(customer.get("balance"))
# print(customer.get("balance",0))
# customer.pop("age")
# print(customer)
# customer.popitem()
# print(customer)
# customer["balance"]=1000
# print(customer)
# customer["age"]=45
# print(customer)
# customer.update({"balance":1000,"phone":343434443})
# print(customer)

for key,value in customer.items():
    print(key)


# customers = [
#         {"name":"John","age":21,"city":"California"},
#         {"name":"Amy","age":22,"city":"Columbus"},
#         {"name":"Mike","age":24,"city":"Jacksonville"}
# ]
# for c in customers:
#     print(c["name"])