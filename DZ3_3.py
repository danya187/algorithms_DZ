def func_hash(user_str):
    system_set = set()
    for el in range(1, len(user_str)):
        for i in range(0, len(user_str)):
            k = user_str[i:i+el]
            system_set.add(hash(k.encode('utf-8')))
    return len(system_set)


user_str = "papa"
print(func_hash(user_str))
