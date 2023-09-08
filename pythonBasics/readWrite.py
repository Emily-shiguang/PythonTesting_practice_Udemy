file = open('test.txt')
# Read all the contents of file
# print(file.read())  # print all
# Read n number of characters by passing parameter
# print(file.read(5))  # print first 5 characters. Space as one character

# print(file.readline())  # read from sixth character. 5 characters have already been read before
# print(file.readline())

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# values = [avc, bd, "cat", dog, elephant]
for line in file.readlines():
    print(line)

file.close()

