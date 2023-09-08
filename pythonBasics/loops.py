greeting = "Good morning"
a = 4
# if greeting == "Morning":
if a > 2:
    print("Condition matches")  # indentation is very, very important in Python
    print("Second line")
else:
    print("Condition does not match")
print("if else condition code is completed")

obj = [1, 2, 3, 4, 5, "haha"]
for i in obj:  # colon
    # print(i)
    print(i*2)


# sum of First Natural numbers 1+2+3+4+5 = 15
summation = 0
for j in range(1, 6):  # range(i, j) -> from i to j-1
    summation = summation + j
print(summation)

print("___________________")
for k in range(1, 10, 2):  # 2 is the step, default is 1
    print(k)

print("___________________")
for m in range(10):  # If you don't give initial index, it starts from 0 -> 0 - 9
    print(m)
