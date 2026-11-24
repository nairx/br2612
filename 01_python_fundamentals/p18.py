result = {
    "John":45,
    "Amy":99,
    "Cathy":57
}

# print(max(result.values()))

print(max(result,key=result.get))


