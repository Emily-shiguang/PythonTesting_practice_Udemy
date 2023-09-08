# List
values = [1, 2, "xz", 9.5]  # List is data type that allows multiple values and can be different data types
print(values[0])  # 1
print(values[3])  # 9.5
print(values[-1])  # 9.5 minus one gives you the last index
print(values[1:3])  # 2 "xz"
print(values)
values.insert(3, "wyb")  # insert
print(values)
values.append("happy")  # append
print(values)
values[2] = "XZ"  # update
print(values)
del values[1]  # delete
print(values)

# Tuple
val = (1, 2, "xz", 9.5)
print(val[1])  # 2

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello world"}
print(dic[4])  # bcd
print(dic["c"])  # Hello world
dict = {}
dict["firstname"] = "Emily"
dict["lastname"] = "Du"
dict["gender"] = "Female"
print(dict)  # {'firstname': 'Emily', 'lastname': 'Du', 'gender': 'Female'}
print(dict["lastname"])  # Du
